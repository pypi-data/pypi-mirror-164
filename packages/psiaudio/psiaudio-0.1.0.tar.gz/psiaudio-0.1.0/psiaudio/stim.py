import logging
log = logging.getLogger(__name__)

import itertools

import numpy as np
from scipy import signal


def fast_cache(f):
    cache = {}
    kwd_marker = object()
    def wrapper(*args, **kw):
        key = args + (kwd_marker,) + tuple(sorted(kw.items()))
        if key not in cache:
            cache[key] = f(*args, **kw)
        return cache[key]
    return wrapper


################################################################################
# Base classes
################################################################################
class Waveform:

    def reset(self):
        raise NotImplementedError

    def next(self, samples):
        raise NotImplementedError

    def n_samples_remaining(self):
        raise NotImplementedError

    def get_samples_remaining(self):
        samples = self.n_samples_remaining()
        if samples == np.inf:
            raise ValueError('Waveform does not have a finite duration')
        return self.next(samples)

    def get_duration(self):
        raise NotImplementedException

    def is_complete(self):
        raise NotImplementedException


class FixedWaveform(Waveform):

    def __init__(self, fs, waveform):
        self.fs = fs
        self.waveform = waveform
        self.reset()

    def reset(self):
        self.offset = 0
        self.complete = False

    def next(self, samples):
        samples = int(samples)
        waveform = self.waveform[self.offset:self.offset+samples]
        waveform_samples = waveform.shape[-1]
        if waveform_samples < samples:
            padding = samples-waveform_samples
            pad = np.zeros(padding)
            waveform = np.concatenate((waveform, pad), axis=-1)
        self.offset += samples
        return waveform

    def n_samples_remaining(self):
        remaining = len(self.waveform)-self.offset
        return np.clip(remaining, 0, np.inf)

    def get_duration(self):
        return len(self.waveform)/self.fs

    def is_complete(self):
        return self.offset >= len(self.waveform)


class Carrier(Waveform):
    '''
    A continuous waveform
    '''

    def get_duration(self):
        return np.inf

    def n_samples_remaining(self):
        return np.inf

    def is_complete(self):
        return False


class Modulator(Waveform):
    '''
    Modulates an input waveform
    '''
    def get_duration(self):
        return self.input_factory.get_duration()

    def n_samples_remaining(self):
        return self.input_factory.n_samples_remaining()

    def is_complete(self):
        return self.input_factory.is_complete()


class GateFactory(Modulator):

    def __init__(self, fs, start_time, duration, input_factory):
        vars(self).update(locals())
        self.start_samples = int(round(start_time * fs))
        self.duration_samples = int(round(self.duration * fs))
        self.total_samples = self.start_samples + self.duration_samples
        self.reset()

    def get_duration(self):
        return self.start_time + self.duration

    def n_samples_remaining(self):
        return max(self.total_samples - self.offset, 0)

    def is_complete(self):
        return self.offset >= self.total_samples

    def reset(self):
        self.offset = 0
        self.input_factory.reset()

    def next(self, samples):
        token = self.input_factory.next(samples)
        lb = self.start_samples - self.offset
        ub = lb + self.duration_samples
        if lb >= 0:
            token[:lb] = 0
        if ub > 0:
            token[ub:] = 0
        self.offset += samples
        return token


################################################################################
# Cos2Envelope
################################################################################
def cos2ramp(t, rise_time, phi=0):
    return np.sin(2*np.pi*t*1.0/rise_time*0.25+phi)**2


@fast_cache
def cos2envelope(fs, duration, rise_time, offset=0, start_time=0,
                 samples='auto'):
    '''
    Generates cosine-squared envelope. Can handle generating fragments (i.e.,
    incomplete sections of the waveform).

    Parameters
    ----------
    fs : float
        Sampling rate
    duration : float
        Duration of envelope (from rise onset to rise offset)
    offset : int
        Offset to begin generating waveform at (in samples relative to start)
    samples : int
        Number of samples to generate for envelope.
    start_time : float
        Start time of envelope
    '''
    if samples == 'auto':
        samples = int(round(duration * fs))

    t = (np.arange(samples, dtype=np.double) + offset)/fs

    m_null_pre = (t < start_time)
    m_onset = (t >= start_time) & (t < (start_time + rise_time))

    # If duration is set to infinite, than we only apply an *onset* ramp.
    # This is used, in particular, for the DPOAE stimulus in which we want
    # to ramp on a continuous tone and then play it continuously until we
    # acquire a sufficient number of epochs.
    if duration != np.inf:
        m_offset = (t >= (start_time+duration-rise_time)) & \
            (t < (start_time+duration))
        m_null_post = t >= (duration+start_time)
    else:
        m_offset = np.zeros_like(t, dtype=np.bool)
        m_null_post = np.zeros_like(t, dtype=np.bool)

    t_null_pre = t[m_null_pre]
    t_onset = t[m_onset] - start_time
    t_offset = t[m_offset] - start_time
    t_ss = t[~(m_null_pre | m_onset | m_offset | m_null_post)]
    t_null_post = t[m_null_post]

    f_null_pre = np.zeros(len(t_null_pre))
    f_lower = cos2ramp(t_onset, rise_time, 0)
    f_upper = cos2ramp(t_offset-(duration-rise_time), rise_time, np.pi/2)
    f_middle = np.ones(len(t_ss))
    f_null_post = np.zeros(len(t_null_post))

    concat = [f_null_pre, f_lower, f_middle, f_upper, f_null_post]
    return np.concatenate(concat, axis=-1)


class Cos2EnvelopeFactory(GateFactory):

    def __init__(self, fs, rise_time, duration, input_factory, start_time=0):
        self.rise_time = rise_time
        super().__init__(fs, start_time, duration, input_factory)

    def next(self, samples):
        token = self.input_factory.next(samples)
        envelope = cos2envelope(self.fs, self.duration, self.rise_time,
                                self.offset, start_time=self.start_time,
                                samples=samples)
        waveform = envelope*token
        self.offset += samples
        return waveform


################################################################################
# SAM envelope
################################################################################
@fast_cache
def sam_eq_power(depth):
    return (3.0/8.0*depth**2.0-depth+1.0)**0.5


@fast_cache
def sam_eq_phase(delay, depth, direction):
    if depth == 0:
        return 0
    z = 2.0/depth*sam_eq_power(depth)-2.0/depth+1
    phi = np.arccos(z)
    return 2.0*np.pi-phi if direction == 1 else phi


@fast_cache
def sam_envelope(offset, samples, fs, depth, fm, delay, eq_phase, eq_power):
    delay_n = np.clip(int(delay*fs)-offset, 0, samples)
    delay_n = int(np.round(delay_n))
    sam_n = samples-delay_n

    sam_offset = offset-delay_n
    t = (np.arange(sam_n, dtype=np.double) + sam_offset)/fs
    sam_envelope = depth/2.0*np.cos(2.0*np.pi*fm*t+eq_phase)+1.0-depth/2.0

    # Ensure that we scale the waveform so that the total power remains equal
    # to that of an unmodulated token.
    sam_envelope *= 1.0/eq_power

    delay_envelope = np.ones(delay_n)
    return np.concatenate((delay_envelope, sam_envelope))


class SAMEnvelopeFactory(Modulator):

    def __init__(self, fs, depth, fm, delay, direction, calibration,
                 input_factory):
        vars(self).update(locals())
        self.eq_phase = sam_eq_phase(delay, depth, direction)
        self.eq_power = sam_eq_power(depth)
        self.reset()

    def reset(self):
        self.offset = 0
        self.input_factory.reset()

    def next(self, samples):
        env = sam_envelope(self.offset, samples, self.fs, self.depth, self.fm,
                           self.delay, self.eq_phase, self.eq_power)
        token = self.input_factory.next(samples)
        waveform = env*token
        self.offset += len(waveform)
        return waveform


################################################################################
# Bandlimited noise
################################################################################
@fast_cache
def _calculate_bandlimited_noise_filter(fs, fl, fh, fls, fhs,
                                        passband_attenuation,
                                        stopband_attenuation):
    Wp = np.array([fl, fh])/(0.5*fs)
    Ws = np.array([fls, fhs])/(0.5*fs)
    b, a = signal.iirdesign(Wp, Ws, passband_attenuation, stopband_attenuation)
    if np.any(np.abs(np.roots(a)) >= 1):
        raise ValueError('Unstable filter coefficients')
    zi = signal.lfilter_zi(b, a)
    return b, a, zi


@fast_cache
def _calculate_bandlimited_noise_iir(fs, calibration, fl, fh):
    duration = 2.0/fl
    iir = calibration.get_iir(fs, fl, fh, duration)
    zi = signal.lfilter_zi(iir, [1])
    return iir, zi


class BandlimitedNoiseFactory(Carrier):
    '''
    Factory for generating continuous bandlimited noise
    '''
    def __init__(self, fs, seed, level, fl, fh, filter_rolloff,
                 passband_attenuation, stopband_attenuation, equalize,
                 calibration):
        vars(self).update(locals())

        # Calculate the scaling factor for the noise
        pass_bandwidth = fh-fl
        self.sf = calibration.get_mean_sf(fl, fh, level)

        # This was copied from the EPL CFT. Need to figure out how this
        # equation works so we can document this better. But it works as
        # intended to scale the noise back to RMS=1.
        self.filter_sf = 1.0/np.sqrt(pass_bandwidth*2/fs/3.0)

        # The RMS value of noise drawn from a uniform distribution is
        # amplitude/sqrt(3). By setting the low and high to sqrt(3) and
        # multiplying by the scaling factors, we can ensure that the noise is
        # initially generated with the desired RMS.
        self.low = -np.sqrt(3)*self.filter_sf*self.sf
        self.high = np.sqrt(3)*self.filter_sf*self.sf

        # Calculate the stop bandwidth as octaves above and below the passband.
        # Precompute the filter settings.
        fls, fhs = fl*(2**-filter_rolloff), fh*(2**filter_rolloff)
        b, a, bp_zi = _calculate_bandlimited_noise_filter(fs, fl, fh, fls, fhs,
                                                          passband_attenuation,
                                                          stopband_attenuation)
        self.b = b
        self.a = a
        self.initial_bp_zi = bp_zi

        # Calculate the IIR filter if we are equalizing the noise.
        if equalize:
            iir, iir_zi = _calculate_bandlimited_noise_iir(fs, calibration, fl, fh)
            self.iir = iir
            self.initial_iir_zi = iir_zi
        else:
            self.iir = None
            self.initial_iir_zi = None

        self.reset()

    def reset(self):
        self.iir_zi = self.initial_iir_zi
        self.bp_zi = self.initial_bp_zi
        self.state = np.random.RandomState(self.seed)

    def next(self, samples):
        waveform = self.state.uniform(low=self.low, high=self.high, size=samples)
        if self.equalize:
            waveform, self.iir_zi = signal.lfilter(self.iir, [1], waveform,
                                                   zi=self.iir_zi)
        waveform, self.bp_zi = signal.lfilter(self.b, self.a, waveform,
                                              zi=self.bp_zi)
        return waveform


################################################################################
# Tone
################################################################################
def tone(fs, frequency, level, phase=0, polarity=1, calibration=None,
         samples='auto', offset=0, duration=None):

    rms = level if calibration is None else calibration.get_sf(frequency, level)
    if samples == 'auto':
        if duration is None:
            raise ValueError('Must provide either duration or samples')
        samples = int(round(duration * fs))
    elif duration is not None:
        raise ValueError('Cannot specify duration if samples is provided')

    # Since the scaling factor is based on Vrms, we need to convert this to the
    # peak-to-peak scaling factor.
    t = (np.arange(samples, dtype=np.double) + offset)/fs
    return polarity * rms * np.sqrt(2) * np.cos(2 * np.pi * t * frequency + phase)


class ToneFactory(Carrier):

    def __init__(self, fs, frequency, level, phase=0, polarity=1,
                 calibration=None):
        vars(self).update(locals())
        self.reset()

    def reset(self):
        self.offset = 0

    def next(self, samples):
        # Note. At least for 5 msec tones it's faster to just compute the array
        # rather than cache the result.
        waveform = tone(self.fs, self.frequency, self.level, self.phase,
                        self.polarity, calibration=self.calibration,
                        offset=self.offset, samples=samples)
        self.offset += samples
        return waveform


################################################################################
# Silence
################################################################################
class SilenceFactory(Carrier):
    '''
    Generate silence

    All channels require at least one continuous output. If no token is
    specified for the continuous output, silence is used.

    Notes
    -----
    The fill_value can be set to a number other than zero for testing (e.g., to
    characterize the effect of a transformation).
    '''

    def __init__(self, fill_value=0):
        self.fill_value = fill_value

    def next(self, samples):
        return np.full(samples, self.fill_value)

    def reset(self):
        pass


################################################################################
# Square waveform
################################################################################
class SquareWaveFactory(Carrier):

    def __init__(self, fs, level, frequency, duty_cycle):
        self.sf = level
        self.cycle_samples = int(round(fs/frequency))
        self.on_samples = int(round(self.cycle_samples * duty_cycle))
        self.reset()

    def reset(self):
        self.offset = 0

    def next(self, samples):
        waveform = np.zeros(samples)
        o = self.offset % self.cycle_samples
        while o < samples:
            waveform[o:o+self.on_samples] = self.sf
            o += self.cycle_samples
        return waveform


################################################################################
# Chirp
################################################################################
class ChirpFactory(FixedWaveform):

    def __init__(self, fs, start_frequency, end_frequency, duration, level,
                 calibration):

        vars(self).update(locals())

        f0 = start_frequency
        f1 = end_frequency

        n = int(fs*duration)
        t = np.arange(n, dtype=np.double) / fs
        k = (end_frequency-start_frequency)/duration

        # Compute instantaneous frequency, which can be used to compute the
        # instantaneous scaling factor for each timepoint (thereby compensating
        # for nonlinearities in the output).
        ifreq = t*k + start_frequency
        sf = calibration.get_sf(ifreq, level)*np.sqrt(2)

        # Now, compute the chirp
        self.waveform = sf*np.sin(2*np.pi*(start_frequency*t + k/2 * t**2))
        self.reset()


################################################################################
# Basic utility functions for the most common use-cases.
################################################################################
def ramped_tone(fs, frequency, level, rise_time, duration, phase=0,
                calibration=None):
    carrier = tone(fs=fs, frequency=frequency, level=level, phase=phase,
                   calibration=calibration, duration=duration)
    env = cos2envelope(fs=fs, rise_time=rise_time, duration=duration)
    return carrier * env

from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def audio_spectrogram(input, window_size, stride, magnitude_squared: bool = ..., name: Any | None = ...): ...

AudioSpectrogram: Any

def audio_spectrogram_eager_fallback(input, window_size, stride, magnitude_squared, name, ctx): ...

class _DecodeWavOutput(NamedTuple):
    audio: Any
    sample_rate: Any

def decode_wav(contents, desired_channels: int = ..., desired_samples: int = ..., name: Any | None = ...): ...

DecodeWav: Any

def decode_wav_eager_fallback(contents, desired_channels, desired_samples, name, ctx): ...
def encode_wav(audio, sample_rate, name: Any | None = ...): ...

EncodeWav: Any

def encode_wav_eager_fallback(audio, sample_rate, name, ctx): ...
def mfcc(spectrogram, sample_rate, upper_frequency_limit: int = ..., lower_frequency_limit: int = ..., filterbank_channel_count: int = ..., dct_coefficient_count: int = ..., name: Any | None = ...): ...

Mfcc: Any

def mfcc_eager_fallback(spectrogram, sample_rate, upper_frequency_limit, lower_frequency_limit, filterbank_channel_count, dct_coefficient_count, name, ctx): ...

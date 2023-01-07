from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.signal import dct_ops as dct_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def mfccs_from_log_mel_spectrograms(log_mel_spectrograms, name: Any | None = ...): ...

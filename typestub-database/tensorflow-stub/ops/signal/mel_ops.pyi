from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.signal import shape_ops as shape_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def linear_to_mel_weight_matrix(num_mel_bins: int = ..., num_spectrogram_bins: int = ..., sample_rate: int = ..., lower_edge_hertz: float = ..., upper_edge_hertz: float = ..., dtype=..., name: Any | None = ...): ...

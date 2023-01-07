from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.ops.signal import fft_ops as fft_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def dct(input, type: int = ..., n: Any | None = ..., axis: int = ..., norm: Any | None = ..., name: Any | None = ...): ...
def idct(input, type: int = ..., n: Any | None = ..., axis: int = ..., norm: Any | None = ..., name: Any | None = ...): ...

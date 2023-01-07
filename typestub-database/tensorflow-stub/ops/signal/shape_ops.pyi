from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.signal import util_ops as util_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def frame(signal, frame_length, frame_step, pad_end: bool = ..., pad_value: int = ..., axis: int = ..., name: Any | None = ...): ...

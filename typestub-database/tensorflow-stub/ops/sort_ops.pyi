from tensorflow.python.framework import constant_op as constant_op, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def sort(values, axis: int = ..., direction: str = ..., name: Any | None = ...): ...
def argsort(values, axis: int = ..., direction: str = ..., stable: bool = ..., name: Any | None = ...): ...

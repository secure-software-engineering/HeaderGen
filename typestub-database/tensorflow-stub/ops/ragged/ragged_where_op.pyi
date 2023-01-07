import typing
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_concat_ops as ragged_concat_ops, ragged_functional_ops as ragged_functional_ops, ragged_gather_ops as ragged_gather_ops, ragged_tensor as ragged_tensor, ragged_tensor_shape as ragged_tensor_shape
from tensorflow.python.util import dispatch as dispatch
from typing import Any

def where_v2(condition: ragged_tensor.RaggedOrDense, x: typing.Optional[ragged_tensor.RaggedOrDense] = ..., y: typing.Optional[ragged_tensor.RaggedOrDense] = ..., name: Any | None = ...): ...
def where(condition: ragged_tensor.RaggedOrDense, x: typing.Optional[ragged_tensor.RaggedOrDense] = ..., y: typing.Optional[ragged_tensor.RaggedOrDense] = ..., name: Any | None = ...): ...

from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.ops.ragged.ragged_tensor import RaggedTensor as RaggedTensor
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from typing import Any

def squeeze(input: ragged_tensor.Ragged, axis: Any | None = ..., name: Any | None = ...): ...

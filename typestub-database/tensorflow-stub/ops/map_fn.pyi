from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def map_fn(fn, elems, dtype: Any | None = ..., parallel_iterations: Any | None = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., name: Any | None = ..., fn_output_signature: Any | None = ...): ...
def map_fn_v2(fn, elems, dtype: Any | None = ..., parallel_iterations: Any | None = ..., back_prop: bool = ..., swap_memory: bool = ..., infer_shape: bool = ..., name: Any | None = ..., fn_output_signature: Any | None = ...): ...

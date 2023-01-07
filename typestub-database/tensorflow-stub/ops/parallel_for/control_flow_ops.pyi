from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import composite_tensor as composite_tensor, indexed_slices as indexed_slices, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.parallel_for.pfor import PFor as PFor, PForConfig as PForConfig
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def for_loop(loop_fn, loop_fn_dtypes, iters, parallel_iterations: Any | None = ...): ...

PFOR_CONFIG_ARG: str

def pfor(loop_fn, iters, fallback_to_while_loop: bool = ..., parallel_iterations: Any | None = ...): ...
def vectorized_map(fn, elems, fallback_to_while_loop: bool = ...): ...

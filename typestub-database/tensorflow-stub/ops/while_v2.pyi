from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import backprop_util as backprop_util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util_v2 as util, default_gradient as default_gradient, gen_functional_ops as gen_functional_ops, gen_resource_variable_ops as gen_resource_variable_ops, gradients_util as gradients_util, handle_data_util as handle_data_util, list_ops as list_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops, while_v2_indexed_slices_rewriter as while_v2_indexed_slices_rewriter
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity
from typing import Any, NamedTuple

glob_stateful_parallelism: bool

def while_loop(cond, body, loop_vars, shape_invariants: Any | None = ..., parallel_iterations: int = ..., maximum_iterations: Any | None = ..., name: Any | None = ..., return_same_structure: bool = ..., back_prop: bool = ...): ...

class OptimizedReductionOpsCacheKey(NamedTuple):
    op_type: Any
    inputs: Any
    dtypes: Any
    input_types: Any
    name: Any
    attrs: Any
    op_def: Any
    compute_device: Any

class _WhileBodyGradFuncGraph(util.WhileBodyFuncGraph):
    extra_inputs: Any
    internal_capture_to_output: Any
    def __init__(self, name, forward_cond_graph, forward_body_graph, maximum_iterations, forward_while_op, body_graph_inputs, body_graph_outputs) -> None: ...
    @property
    def while_op_needs_rewrite(self): ...

class _OperationWithOutputs(ops.Operation):
    def __init__(self, c_op, g) -> None: ...

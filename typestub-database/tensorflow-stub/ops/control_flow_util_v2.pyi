from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import function_def_to_graph as function_def_to_graph, ops as ops
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.ops import control_flow_util as control_flow_util, control_flow_v2_func_graphs as control_flow_v2_func_graphs, gradients_util as gradients_util
from tensorflow.python.util import keras_deps as keras_deps, tf_contextlib as tf_contextlib
from typing import Any

CondBranchFuncGraph: Any
WhileCondFuncGraph: Any
WhileBodyFuncGraph: Any

def in_defun(): ...
def in_while_loop_defun(graph): ...
def create_new_tf_function(func_graph): ...
def unique_fn_name(scope, name): ...
def unique_grad_fn_name(forward_name): ...
def maybe_set_lowering_attr(op, lower_using_switch_merge: Any | None = ...) -> None: ...
def maybe_propagate_compile_time_consts_in_xla(op) -> None: ...
def resource_input_index(tensor_name, input_names, node_defs, functions): ...
def clear_control_inputs() -> None: ...
def output_all_intermediates(): ...
def get_func_graph(op, input_shapes, func_name): ...
def get_op_and_outputs(op_or_outputs): ...
def graph_wrapped_for_higher_order_tape_gradients(graph): ...
def run_as_function_for_tape_gradients(make_op, inputs): ...

from tensorflow.python.framework import func_graph as func_graph, ops as ops
from tensorflow.python.ops import array_ops as array_ops, op_selector as op_selector, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

UnliftableError: Any

class _InputMutation(NamedTuple):
    copied_op: Any
    input_index: Any
    old_graph_tensor: Any

class _ControlMutation(NamedTuple):
    copied_op: Any
    old_graph_op: Any

def lift_to_graph(tensors, graph, sources: Any | None = ..., disallowed_placeholders: Any | None = ..., add_sources: bool = ..., handle_captures: bool = ..., base_graph: Any | None = ..., op_map: Any | None = ...): ...

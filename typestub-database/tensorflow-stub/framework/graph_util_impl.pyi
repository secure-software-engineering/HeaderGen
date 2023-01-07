from tensorflow.core.framework import graph_pb2 as graph_pb2, node_def_pb2 as node_def_pb2
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.util import deprecation as deprecation, lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

convert_to_constants: Any

def must_run_on_cpu(node, pin_variables_on_cpu: bool = ...): ...
def extract_sub_graph(graph_def, dest_nodes): ...
def tensor_shape_from_node_def_name(graph, input_name): ...
def convert_variables_to_constants(sess, input_graph_def, output_node_names, variable_names_whitelist: Any | None = ..., variable_names_blacklist: Any | None = ...): ...
def remove_training_nodes(input_graph, protected_nodes: Any | None = ...): ...
def graph_defs_equal(graph_def_1: graph_pb2.GraphDef, graph_def_2: graph_pb2.GraphDef, treat_nan_as_equal: bool = ...) -> bool: ...

from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import c_api_util as c_api_util, errors as errors, function as function, op_def_registry as op_def_registry, ops as ops
from tensorflow.python.ops import control_flow_util as control_flow_util
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def import_graph_def(graph_def, input_map: Any | None = ..., return_elements: Any | None = ..., name: Any | None = ..., op_dict: Any | None = ..., producer_op_list: Any | None = ...): ...
def import_graph_def_for_function(graph_def, name: Any | None = ...): ...

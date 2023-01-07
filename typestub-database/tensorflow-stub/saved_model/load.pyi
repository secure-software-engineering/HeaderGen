from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from tensorflow.python.distribute import distribute_utils as distribute_utils, values_util as values_util
from tensorflow.python.eager import context as context, def_function as def_function, function as function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, handle_data_util as handle_data_util, lookup_ops as lookup_ops, resource_variable_ops as resource_variable_ops, variables as variables
from tensorflow.python.saved_model import function_deserialization as function_deserialization, load_options as load_options, load_v1_in_v2 as load_v1_in_v2, loader_impl as loader_impl, nested_structure_coder as nested_structure_coder, registration as registration, revived_types as revived_types
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.training.saving import checkpoint_options as checkpoint_options, saveable_object_util as saveable_object_util
from tensorflow.python.training.tracking import base as base, data_structures as data_structures, graph_view as graph_view, tracking as tracking, util as util
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class _WrapperFunction(function.ConcreteFunction):
    def __init__(self, concrete_function) -> None: ...

class Loader:
    def __init__(self, object_graph_proto, saved_model_proto, export_dir, ckpt_options, save_options, filters) -> None: ...
    def adjust_debug_info_func_names(self, debug_info): ...
    def get(self, node_id): ...

class _RestoredResource(tracking.TrackableResource):
    def __init__(self, device: str = ...) -> None: ...

def load_partial(export_dir, filters, tags: Any | None = ..., options: Any | None = ...): ...
def load(export_dir, tags: Any | None = ..., options: Any | None = ...): ...
def load_internal(export_dir, tags: Any | None = ..., options: Any | None = ..., loader_cls=..., filters: Any | None = ...): ...

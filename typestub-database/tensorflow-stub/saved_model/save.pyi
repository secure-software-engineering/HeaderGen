from tensorflow.core.framework import function_pb2 as function_pb2, versions_pb2 as versions_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, saved_model_pb2 as saved_model_pb2, saved_object_graph_pb2 as saved_object_graph_pb2
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, error_interpolation as error_interpolation, errors as errors, meta_graph as meta_graph, ops as ops, tensor_util as tensor_util, versions as versions
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import builder_impl as builder_impl, function_serialization as function_serialization, nested_structure_coder as nested_structure_coder, pywrap_saved_model as pywrap_saved_model, registration as registration, revived_types as revived_types, save_context as save_context, save_options as save_options, signature_constants as signature_constants, signature_def_utils as signature_def_utils, signature_serialization as signature_serialization, tag_constants as tag_constants, utils_impl as utils_impl
from tensorflow.python.saved_model.pywrap_saved_model import constants as constants, metrics as metrics
from tensorflow.python.training.saving import checkpoint_options as checkpoint_options, functional_saver as functional_saver, saveable_object_util as saveable_object_util
from tensorflow.python.training.tracking import base as base, graph_view as graph_view, tracking as tracking, util as util
from tensorflow.python.util import compat as compat, object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _CapturedConstant(NamedTuple):
    eager_tensor: Any
    graph_tensor: Any

class _CapturedTensor(NamedTuple):
    name: Any
    concrete_function: Any

class _AugmentedGraphView(graph_view.ObjectGraphView):
    def __init__(self, root) -> None: ...
    def add_object(self, parent_node, name_in_parent, subgraph_root) -> None: ...
    def list_dependencies(self, obj) -> None: ...
    def list_extra_dependencies(self, obj): ...
    def list_functions(self, obj): ...

class _SaveableView:
    checkpoint_view: Any
    function_name_map: Any
    captured_tensor_node_ids: Any
    def __init__(self, checkpoint_view, options, wrapped_functions: Any | None = ...) -> None: ...
    @property
    def concrete_and_gradient_functions(self): ...
    @property
    def root(self): ...
    def fill_object_graph_proto(self, proto) -> None: ...
    concrete_functions: Any
    def map_resources(self): ...
    def add_capture_and_node(self, capture, node): ...

class _AssetInfo(NamedTuple):
    asset_defs: Any
    asset_initializers_by_resource: Any
    asset_filename_map: Any
    asset_index: Any

def save(obj, export_dir, signatures: Any | None = ..., options: Any | None = ...) -> None: ...
def save_and_return_nodes(obj, export_dir, signatures: Any | None = ..., options: Any | None = ..., experimental_skip_checkpoint: bool = ...): ...
def export_meta_graph(obj, filename, signatures: Any | None = ..., options: Any | None = ...) -> None: ...

from google.protobuf.any_pb2 import Any
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, graph_pb2 as graph_pb2, op_def_pb2 as op_def_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, saver_pb2 as saver_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import error_interpolation as error_interpolation, graph_io as graph_io, importer as importer, op_def_registry as op_def_registry, ops as ops, versions as versions
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.util import compat as compat

def ops_used_by_graph_def(graph_def): ...
def stripped_op_list_for_graph(graph_def): ...

SAVE_AND_RESTORE_OPS: Any

def add_collection_def(meta_graph_def, key, graph: Any | None = ..., export_scope: Any | None = ..., exclude_nodes: Any | None = ..., override_contents: Any | None = ...) -> None: ...
def strip_graph_default_valued_attrs(meta_graph_def) -> None: ...
def create_meta_graph_def(meta_info_def: Any | None = ..., graph_def: Any | None = ..., saver_def: Any | None = ..., collection_list: Any | None = ..., graph: Any | None = ..., export_scope: Any | None = ..., exclude_nodes: Any | None = ..., clear_extraneous_savers: bool = ..., strip_default_attrs: bool = ...): ...
def read_meta_graph_file(filename): ...
def import_scoped_meta_graph(meta_graph_or_file, clear_devices: bool = ..., graph: Any | None = ..., import_scope: Any | None = ..., input_map: Any | None = ..., unbound_inputs_col_name: str = ..., restore_collections_predicate=...): ...
def import_scoped_meta_graph_with_return_elements(meta_graph_or_file, clear_devices: bool = ..., graph: Any | None = ..., import_scope: Any | None = ..., input_map: Any | None = ..., unbound_inputs_col_name: str = ..., restore_collections_predicate=..., return_elements: Any | None = ...): ...
def export_scoped_meta_graph(filename: Any | None = ..., graph_def: Any | None = ..., graph: Any | None = ..., export_scope: Any | None = ..., as_text: bool = ..., unbound_inputs_col_name: str = ..., clear_devices: bool = ..., saver_def: Any | None = ..., clear_extraneous_savers: bool = ..., strip_default_attrs: bool = ..., save_debug_info: bool = ..., **kwargs): ...
def copy_scoped_meta_graph(from_scope, to_scope, from_graph: Any | None = ..., to_graph: Any | None = ...): ...

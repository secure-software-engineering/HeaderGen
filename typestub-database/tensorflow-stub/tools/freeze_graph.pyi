from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import saver_pb2 as saver_pb2
from tensorflow.core.protobuf.meta_graph_pb2 import MetaGraphDef as MetaGraphDef
from tensorflow.python.client import session as session
from tensorflow.python.framework import graph_util as graph_util, importer as importer
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import loader as loader, tag_constants as tag_constants
from tensorflow.python.tools import saved_model_utils as saved_model_utils
from tensorflow.python.training import checkpoint_management as checkpoint_management, py_checkpoint_reader as py_checkpoint_reader
from typing import Any

def freeze_graph_with_def_protos(input_graph_def, input_saver_def, input_checkpoint, output_node_names, restore_op_name, filename_tensor_name, output_graph, clear_devices, initializer_nodes, variable_names_whitelist: str = ..., variable_names_denylist: str = ..., input_meta_graph_def: Any | None = ..., input_saved_model_dir: Any | None = ..., saved_model_tags: Any | None = ..., checkpoint_version=...): ...
def freeze_graph(input_graph, input_saver, input_binary, input_checkpoint, output_node_names, restore_op_name, filename_tensor_name, output_graph, clear_devices, initializer_nodes, variable_names_whitelist: str = ..., variable_names_denylist: str = ..., input_meta_graph: Any | None = ..., input_saved_model_dir: Any | None = ..., saved_model_tags=..., checkpoint_version=...): ...
def main(unused_args, flags) -> None: ...
def run_main(): ...

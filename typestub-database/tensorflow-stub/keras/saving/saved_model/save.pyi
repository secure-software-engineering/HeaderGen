from tensorflow.python.keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2, versions_pb2 as versions_pb2
from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import constants as constants, save_impl as save_impl, utils as utils
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.platform import gfile as gfile
from typing import Any

base_layer: Any
training_lib: Any

def save(model, filepath, overwrite, include_optimizer, signatures: Any | None = ..., options: Any | None = ..., save_traces: bool = ...) -> None: ...
def generate_keras_metadata(saved_nodes, node_paths): ...

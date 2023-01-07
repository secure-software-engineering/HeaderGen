from keras import backend as backend
from keras.layers import serialization as serialization
from keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2, versions_pb2 as versions_pb2
from keras.saving import saving_utils as saving_utils
from keras.saving.saved_model import constants as constants, save_impl as save_impl, utils as utils
from keras.utils.generic_utils import LazyLoader as LazyLoader
from keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from typing import Any

base_layer: Any
training_lib: Any

def save(model, filepath, overwrite, include_optimizer, signatures: Any | None = ..., options: Any | None = ..., save_traces: bool = ...) -> None: ...
def generate_keras_metadata(saved_nodes, node_paths): ...

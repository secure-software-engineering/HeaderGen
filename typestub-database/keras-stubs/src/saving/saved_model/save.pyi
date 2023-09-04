from typing import Any

from keras import backend as backend
from keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2
from keras.protobuf import versions_pb2 as versions_pb2
from keras.src.layers import serialization as serialization
from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import constants as constants
from keras.src.saving.saved_model import save_impl as save_impl
from keras.src.saving.saved_model import utils as utils
from keras.utils.generic_utils import LazyLoader as LazyLoader
from keras.utils.io_utils import (
    ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite,
)

base_layer: Any
training_lib: Any

def save(
    model,
    filepath,
    overwrite,
    include_optimizer,
    signatures: Any | None = ...,
    options: Any | None = ...,
    save_traces: bool = ...,
) -> None: ...
def generate_keras_metadata(saved_nodes, node_paths): ...

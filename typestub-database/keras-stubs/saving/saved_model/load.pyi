from keras import backend as backend, regularizers as regularizers
from keras.engine import input_spec as input_spec
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2, versions_pb2 as versions_pb2
from keras.saving import saving_utils as saving_utils
from keras.saving.saved_model import constants as constants, json_utils as json_utils, utils as utils
from keras.saving.saved_model.serialized_attributes import CommonEndpoints as CommonEndpoints
from keras.utils import generic_utils as generic_utils, metrics_utils as metrics_utils
from keras.utils.generic_utils import LazyLoader as LazyLoader
from typing import Any

models_lib: Any
base_layer: Any
layers_module: Any
input_layer: Any
functional_lib: Any
training_lib: Any
training_lib_v1: Any
metrics: Any
recurrent: Any
PUBLIC_ATTRIBUTES: Any

def load(path, compile: bool = ..., options: Any | None = ...): ...

class KerasObjectLoader:
    loaded_nodes: Any
    model_layer_dependencies: Any
    def __init__(self, metadata, object_graph_def) -> None: ...
    def del_tracking(self) -> None: ...
    def load_layers(self, compile: bool = ...) -> None: ...
    def get_path(self, node_id): ...
    def finalize_objects(self) -> None: ...

def revive_custom_object(identifier, metadata): ...

class RevivedLayer:
    @property
    def keras_api(self): ...
    def get_config(self): ...

class RevivedInputLayer:
    def get_config(self): ...

def recursively_deserialize_keras_object(config, module_objects: Any | None = ...): ...
def infer_inputs_from_restored_call_function(fn): ...

class RevivedNetwork(RevivedLayer): ...

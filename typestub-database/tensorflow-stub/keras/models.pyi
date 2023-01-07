from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend, optimizer_v1 as optimizer_v1
from tensorflow.python.keras.engine import functional as functional, sequential as sequential, training as training, training_v1 as training_v1
from tensorflow.python.keras.engine.base_layer import AddMetric as AddMetric, Layer as Layer
from tensorflow.python.keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from tensorflow.python.keras.saving import model_config as model_config, save as save
from tensorflow.python.keras.utils import generic_utils as generic_utils, version_utils as version_utils
from tensorflow.python.keras.utils.generic_utils import CustomObjectScope as CustomObjectScope
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

Model: Any
Sequential: Any
Functional: Any
save_model: Any
load_model: Any
model_from_config: Any
model_from_yaml: Any
model_from_json: Any

def share_weights(layer): ...
def clone_model(model, input_tensors: Any | None = ..., clone_function: Any | None = ...): ...
def in_place_subclassed_model_state_restoration(model) -> None: ...
def clone_and_build_model(model, input_tensors: Any | None = ..., target_tensors: Any | None = ..., custom_objects: Any | None = ..., compile_clone: bool = ..., in_place_reset: bool = ..., optimizer_iterations: Any | None = ..., optimizer_config: Any | None = ...): ...

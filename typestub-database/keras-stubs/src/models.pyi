from typing import Any

from keras import backend as backend
from keras import optimizer_v1 as optimizer_v1
from keras.src.engine import functional as functional
from keras.src.engine import sequential as sequential
from keras.src.engine import training as training
from keras.src.engine import training_v1 as training_v1
from keras.src.engine.base_layer import AddMetric as AddMetric
from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.input_layer import Input as Input
from keras.src.engine.input_layer import InputLayer as InputLayer
from keras.src.saving import model_config as model_config
from keras.src.saving import save as save
from keras.utils import generic_utils as generic_utils
from keras.utils import version_utils as version_utils
from keras.utils.generic_utils import CustomObjectScope as CustomObjectScope

Model = training.Model
Sequential = sequential.Sequential
Functional = functional.Functional
save_model = save.save_model
load_model = save.load_model
model_from_config = model_config.model_from_config
model_from_yaml = model_config.model_from_yaml
model_from_json = model_config.model_from_json

def share_weights(layer): ...
def clone_model(
    model, input_tensors: Any | None = ..., clone_function: Any | None = ...
): ...
def in_place_subclassed_model_state_restoration(model) -> None: ...
def clone_and_build_model(
    model,
    input_tensors: Any | None = ...,
    target_tensors: Any | None = ...,
    custom_objects: Any | None = ...,
    compile_clone: bool = ...,
    in_place_reset: bool = ...,
    optimizer_iterations: Any | None = ...,
    optimizer_config: Any | None = ...,
): ...

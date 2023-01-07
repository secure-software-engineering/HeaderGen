from keras import backend as backend
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils
from typing import Any

BASE_WEIGHT_PATH: str
layers: Any

def MobileNet(input_shape: Any | None = ..., alpha: float = ..., depth_multiplier: int = ..., dropout: float = ..., include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ..., **kwargs): ...
def preprocess_input(x, data_format: Any | None = ...): ...
def decode_predictions(preds, top: int = ...): ...

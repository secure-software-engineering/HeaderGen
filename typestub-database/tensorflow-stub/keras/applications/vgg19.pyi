from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.layers import VersionAwareLayers as VersionAwareLayers
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

WEIGHTS_PATH: str
WEIGHTS_PATH_NO_TOP: str
layers: Any

def VGG19(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ...): ...
def preprocess_input(x, data_format: Any | None = ...): ...
def decode_predictions(preds, top: int = ...): ...

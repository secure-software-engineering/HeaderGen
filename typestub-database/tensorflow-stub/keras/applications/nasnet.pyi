from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.layers import VersionAwareLayers as VersionAwareLayers
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

BASE_WEIGHTS_PATH: str
NASNET_MOBILE_WEIGHT_PATH: Any
NASNET_MOBILE_WEIGHT_PATH_NO_TOP: Any
NASNET_LARGE_WEIGHT_PATH: Any
NASNET_LARGE_WEIGHT_PATH_NO_TOP: Any
layers: Any

def NASNet(input_shape: Any | None = ..., penultimate_filters: int = ..., num_blocks: int = ..., stem_block_filters: int = ..., skip_reduction: bool = ..., filter_multiplier: int = ..., include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., pooling: Any | None = ..., classes: int = ..., default_size: Any | None = ..., classifier_activation: str = ...): ...
def NASNetMobile(input_shape: Any | None = ..., include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., pooling: Any | None = ..., classes: int = ...): ...
def NASNetLarge(input_shape: Any | None = ..., include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., pooling: Any | None = ..., classes: int = ...): ...
def preprocess_input(x, data_format: Any | None = ...): ...
def decode_predictions(preds, top: int = ...): ...

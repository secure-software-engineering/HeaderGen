from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils
from tensorflow.python.keras.engine import training as training
from tensorflow.python.keras.layers import VersionAwareLayers as VersionAwareLayers
from tensorflow.python.keras.utils import data_utils as data_utils, layer_utils as layer_utils
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Any
layers: Any

def ResNet(stack_fn, preact, use_bias, model_name: str = ..., include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ..., **kwargs): ...
def block1(x, filters, kernel_size: int = ..., stride: int = ..., conv_shortcut: bool = ..., name: Any | None = ...): ...
def stack1(x, filters, blocks, stride1: int = ..., name: Any | None = ...): ...
def block2(x, filters, kernel_size: int = ..., stride: int = ..., conv_shortcut: bool = ..., name: Any | None = ...): ...
def stack2(x, filters, blocks, stride1: int = ..., name: Any | None = ...): ...
def block3(x, filters, kernel_size: int = ..., stride: int = ..., groups: int = ..., conv_shortcut: bool = ..., name: Any | None = ...): ...
def stack3(x, filters, blocks, stride1: int = ..., groups: int = ..., name: Any | None = ...): ...
def ResNet50(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., **kwargs): ...
def ResNet101(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., **kwargs): ...
def ResNet152(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., **kwargs): ...
def preprocess_input(x, data_format: Any | None = ...): ...
def decode_predictions(preds, top: int = ...): ...

DOC: str

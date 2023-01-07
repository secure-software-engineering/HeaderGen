from tensorflow.python.keras.applications import imagenet_utils as imagenet_utils, resnet as resnet
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def ResNet50V2(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ...): ...
def ResNet101V2(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ...): ...
def ResNet152V2(include_top: bool = ..., weights: str = ..., input_tensor: Any | None = ..., input_shape: Any | None = ..., pooling: Any | None = ..., classes: int = ..., classifier_activation: str = ...): ...
def preprocess_input(x, data_format: Any | None = ...): ...
def decode_predictions(preds, top: int = ...): ...

DOC: str

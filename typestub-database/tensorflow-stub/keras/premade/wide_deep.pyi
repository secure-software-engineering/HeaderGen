from tensorflow.python.eager import backprop as backprop
from tensorflow.python.keras import activations as activations, backend as backend
from tensorflow.python.keras.engine import base_layer as base_layer, data_adapter as data_adapter, training as keras_training
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class WideDeepModel(keras_training.Model):
    linear_model: Any
    dnn_model: Any
    activation: Any
    def __init__(self, linear_model, dnn_model, activation: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs, training: Any | None = ...): ...
    def train_step(self, data): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

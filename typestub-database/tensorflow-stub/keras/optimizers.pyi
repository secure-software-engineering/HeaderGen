from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.optimizer_v1 import Optimizer as Optimizer, TFOptimizer as TFOptimizer
from tensorflow.python.keras.optimizer_v2 import ftrl as ftrl, optimizer_v2 as optimizer_v2
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

def serialize(optimizer): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get(identifier): ...

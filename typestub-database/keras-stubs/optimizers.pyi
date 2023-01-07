from keras import backend as backend
from keras.optimizer_v1 import Optimizer as Optimizer, TFOptimizer as TFOptimizer
from keras.optimizer_v2 import ftrl as ftrl, optimizer_v2 as optimizer_v2
from keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object
from typing import Any

def serialize(optimizer): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get(identifier): ...

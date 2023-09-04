from typing import Any

from keras import backend as backend
from keras.optimizer_v1 import Optimizer as Optimizer
from keras.optimizer_v1 import TFOptimizer as TFOptimizer
from keras.optimizer_v2 import ftrl as ftrl
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from keras.utils.generic_utils import (
    deserialize_keras_object as deserialize_keras_object,
)
from keras.utils.generic_utils import serialize_keras_object as serialize_keras_object

def serialize(optimizer): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get(identifier): ...

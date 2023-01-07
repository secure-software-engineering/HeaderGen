from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend_config as backend_config
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.training import gen_training_ops as gen_training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Adadelta(optimizer_v2.OptimizerV2):
    epsilon: Any
    def __init__(self, learning_rate: float = ..., rho: float = ..., epsilon: float = ..., name: str = ..., **kwargs) -> None: ...
    def set_weights(self, weights) -> None: ...
    def get_config(self): ...

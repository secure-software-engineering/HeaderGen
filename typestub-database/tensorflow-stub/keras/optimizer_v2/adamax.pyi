from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras import backend_config as backend_config
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.training import gen_training_ops as gen_training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class Adamax(optimizer_v2.OptimizerV2):
    epsilon: Any
    def __init__(self, learning_rate: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., name: str = ..., **kwargs) -> None: ...
    def get_config(self): ...

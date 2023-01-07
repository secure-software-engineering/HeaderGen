from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops
from tensorflow.python.training import gen_training_ops as gen_training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

class Ftrl(optimizer_v2.OptimizerV2):
    def __init__(self, learning_rate: float = ..., learning_rate_power=..., initial_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., name: str = ..., l2_shrinkage_regularization_strength: float = ..., beta: float = ..., **kwargs) -> None: ...
    def get_config(self): ...

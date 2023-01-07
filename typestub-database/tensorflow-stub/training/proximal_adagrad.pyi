from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class ProximalAdagradOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate, initial_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_locking: bool = ..., name: str = ...) -> None: ...

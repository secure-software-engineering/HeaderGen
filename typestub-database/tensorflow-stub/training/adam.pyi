from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdamOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate: float = ..., beta1: float = ..., beta2: float = ..., epsilon: float = ..., use_locking: bool = ..., name: str = ...) -> None: ...

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class RMSPropOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate, decay: float = ..., momentum: float = ..., epsilon: float = ..., use_locking: bool = ..., centered: bool = ..., name: str = ...) -> None: ...

from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, init_ops as init_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdagradOptimizer(optimizer.Optimizer):
    def __init__(self, learning_rate, initial_accumulator_value: float = ..., use_locking: bool = ..., name: str = ...) -> None: ...

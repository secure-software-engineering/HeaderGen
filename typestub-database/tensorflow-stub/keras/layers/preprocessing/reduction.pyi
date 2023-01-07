from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from typing import Any

def get_reduce_op(reduction_str): ...

class Reduction(Layer):
    reduction: Any
    axis: Any
    def __init__(self, reduction, axis: int = ..., **kwargs) -> None: ...
    def call(self, inputs, weights: Any | None = ...): ...

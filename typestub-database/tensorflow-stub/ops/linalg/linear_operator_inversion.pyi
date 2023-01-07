from tensorflow.python.framework import ops as ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_util as linear_operator_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class LinearOperatorInversion(linear_operator.LinearOperator):
    def __init__(self, operator, is_non_singular: Any | None = ..., is_self_adjoint: Any | None = ..., is_positive_definite: Any | None = ..., is_square: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def operator(self): ...

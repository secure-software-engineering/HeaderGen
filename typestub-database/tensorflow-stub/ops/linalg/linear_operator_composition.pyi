from tensorflow.python.ops.linalg import linear_operator
from typing import Any

class LinearOperatorComposition(linear_operator.LinearOperator):
    def __init__(self, operators, is_non_singular: Any | None = ..., is_self_adjoint: Any | None = ..., is_positive_definite: Any | None = ..., is_square: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def operators(self): ...

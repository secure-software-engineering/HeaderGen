from tensorflow.python.ops.linalg import linear_operator
from typing import Any

class LinearOperatorFullMatrix(linear_operator.LinearOperator):
    def __init__(self, matrix, is_non_singular: Any | None = ..., is_self_adjoint: Any | None = ..., is_positive_definite: Any | None = ..., is_square: Any | None = ..., name: str = ...) -> None: ...

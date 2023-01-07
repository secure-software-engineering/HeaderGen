import abc
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from tensorflow.python.ops.linalg import linear_operator as linear_operator, linear_operator_diag as linear_operator_diag, linear_operator_full_matrix as linear_operator_full_matrix, linear_operator_identity as linear_operator_identity, linear_operator_lower_triangular as linear_operator_lower_triangular
from typing import Any

def add_operators(operators, operator_name: Any | None = ..., addition_tiers: Any | None = ..., name: Any | None = ...): ...

class _Hints:
    is_non_singular: Any
    is_positive_definite: Any
    is_self_adjoint: Any
    def __init__(self, is_non_singular: Any | None = ..., is_positive_definite: Any | None = ..., is_self_adjoint: Any | None = ...) -> None: ...

class _Adder(metaclass=abc.ABCMeta):
    @property
    def name(self): ...
    @abc.abstractmethod
    def can_add(self, op1, op2): ...
    def add(self, op1, op2, operator_name, hints: Any | None = ...): ...

class _AddAndReturnScaledIdentity(_Adder):
    def can_add(self, op1, op2): ...

class _AddAndReturnDiag(_Adder):
    def can_add(self, op1, op2): ...

class _AddAndReturnTriL(_Adder):
    def can_add(self, op1, op2): ...

class _AddAndReturnMatrix(_Adder):
    def can_add(self, op1, op2): ...

SUPPORTED_OPERATORS: Any

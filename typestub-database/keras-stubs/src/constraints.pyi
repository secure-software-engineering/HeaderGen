from typing import Any

from keras import backend as backend
from keras.utils.generic_utils import (
    deserialize_keras_object as deserialize_keras_object,
)
from keras.utils.generic_utils import serialize_keras_object as serialize_keras_object

class Constraint:
    def __call__(self, w): ...
    def get_config(self): ...

class MaxNorm(Constraint):
    max_value: Any
    axis: Any
    def __init__(self, max_value: int = ..., axis: int = ...) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class NonNeg(Constraint):
    def __call__(self, w): ...

class UnitNorm(Constraint):
    axis: Any
    def __init__(self, axis: int = ...) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class MinMaxNorm(Constraint):
    min_value: Any
    max_value: Any
    rate: Any
    axis: Any
    def __init__(
        self,
        min_value: float = ...,
        max_value: float = ...,
        rate: float = ...,
        axis: int = ...,
    ) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class RadialConstraint(Constraint):
    def __call__(self, w): ...

max_norm = MaxNorm
non_neg = NonNeg
unit_norm = UnitNorm
min_max_norm = MinMaxNorm
radial_constraint = RadialConstraint
maxnorm = max_norm
nonneg = non_neg
unitnorm = unit_norm

def serialize(constraint): ...
def deserialize(config, custom_objects: Any | None = ...): ...
def get(identifier): ...

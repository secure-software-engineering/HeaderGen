import abc
from keras import backend as backend
from keras.utils import generic_utils as generic_utils
from typing import Any

class LearningRateSchedule(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, step): ...
    @abc.abstractmethod
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class ExponentialDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    decay_rate: Any
    staircase: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase: bool = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class PiecewiseConstantDecay(LearningRateSchedule):
    boundaries: Any
    values: Any
    name: Any
    def __init__(self, boundaries, values, name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class PolynomialDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    end_learning_rate: Any
    power: Any
    cycle: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, end_learning_rate: float = ..., power: float = ..., cycle: bool = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class InverseTimeDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    decay_rate: Any
    staircase: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase: bool = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class CosineDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    alpha: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, alpha: float = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class CosineDecayRestarts(LearningRateSchedule):
    initial_learning_rate: Any
    first_decay_steps: Any
    alpha: Any
    name: Any
    def __init__(self, initial_learning_rate, first_decay_steps, t_mul: float = ..., m_mul: float = ..., alpha: float = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class LinearCosineDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    num_periods: Any
    alpha: Any
    beta: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, num_periods: float = ..., alpha: float = ..., beta: float = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

class NoisyLinearCosineDecay(LearningRateSchedule):
    initial_learning_rate: Any
    decay_steps: Any
    initial_variance: Any
    variance_decay: Any
    num_periods: Any
    alpha: Any
    beta: Any
    seed: Any
    name: Any
    def __init__(self, initial_learning_rate, decay_steps, initial_variance: float = ..., variance_decay: float = ..., num_periods: float = ..., alpha: float = ..., beta: float = ..., seed: Any | None = ..., name: Any | None = ...) -> None: ...
    def __call__(self, step): ...
    def get_config(self): ...

def serialize(learning_rate_schedule): ...
def deserialize(config, custom_objects: Any | None = ...): ...

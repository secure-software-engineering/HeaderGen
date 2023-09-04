import abc
from typing import Any

from keras import backend as backend
from keras.utils import losses_utils as losses_utils
from keras.utils import tf_utils as tf_utils
from keras.utils.generic_utils import (
    deserialize_keras_object as deserialize_keras_object,
)
from keras.utils.generic_utils import serialize_keras_object as serialize_keras_object

class Loss(metaclass=abc.ABCMeta):
    reduction: Any
    name: Any
    def __init__(self, reduction=..., name: Any | None = ...) -> None: ...
    def __call__(self, y_true, y_pred, sample_weight: Any | None = ...): ...
    @classmethod
    def from_config(cls, config): ...
    def get_config(self): ...
    @abc.abstractmethod
    def call(self, y_true, y_pred): ...

class LossFunctionWrapper(Loss):
    fn: Any
    def __init__(self, fn, reduction=..., name: Any | None = ..., **kwargs) -> None: ...
    def call(self, y_true, y_pred): ...
    def get_config(self): ...

class MeanSquaredError(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class MeanAbsoluteError(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class MeanAbsolutePercentageError(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class MeanSquaredLogarithmicError(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class BinaryCrossentropy(LossFunctionWrapper):
    from_logits: Any
    def __init__(
        self,
        from_logits: bool = ...,
        label_smoothing: float = ...,
        axis: int = ...,
        reduction=...,
        name: str = ...,
    ) -> None: ...

class BinaryFocalCrossentropy(LossFunctionWrapper):
    from_logits: Any
    gamma: Any
    def __init__(
        self,
        gamma: float = ...,
        from_logits: bool = ...,
        label_smoothing: float = ...,
        axis: int = ...,
        reduction=...,
        name: str = ...,
    ) -> None: ...
    def get_config(self): ...

class CategoricalCrossentropy(LossFunctionWrapper):
    def __init__(
        self,
        from_logits: bool = ...,
        label_smoothing: float = ...,
        axis: int = ...,
        reduction=...,
        name: str = ...,
    ) -> None: ...

class SparseCategoricalCrossentropy(LossFunctionWrapper):
    def __init__(
        self, from_logits: bool = ..., reduction=..., name: str = ...
    ) -> None: ...

class Hinge(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class SquaredHinge(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class CategoricalHinge(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class Poisson(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class LogCosh(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class KLDivergence(LossFunctionWrapper):
    def __init__(self, reduction=..., name: str = ...) -> None: ...

class Huber(LossFunctionWrapper):
    def __init__(self, delta: float = ..., reduction=..., name: str = ...) -> None: ...

def mean_squared_error(y_true, y_pred): ...
def mean_absolute_error(y_true, y_pred): ...
def mean_absolute_percentage_error(y_true, y_pred): ...
def mean_squared_logarithmic_error(y_true, y_pred): ...
def squared_hinge(y_true, y_pred): ...
def hinge(y_true, y_pred): ...
def categorical_hinge(y_true, y_pred): ...
def huber(y_true, y_pred, delta: float = ...): ...
def log_cosh(y_true, y_pred): ...
def categorical_crossentropy(
    y_true,
    y_pred,
    from_logits: bool = ...,
    label_smoothing: float = ...,
    axis: int = ...,
): ...
def sparse_categorical_crossentropy(
    y_true, y_pred, from_logits: bool = ..., axis: int = ...
): ...
def binary_crossentropy(
    y_true,
    y_pred,
    from_logits: bool = ...,
    label_smoothing: float = ...,
    axis: int = ...,
): ...
def binary_focal_crossentropy(
    y_true,
    y_pred,
    gamma: float = ...,
    from_logits: bool = ...,
    label_smoothing: float = ...,
    axis: int = ...,
): ...
def kl_divergence(y_true, y_pred): ...
def poisson(y_true, y_pred): ...
def cosine_similarity(y_true, y_pred, axis: int = ...): ...

class CosineSimilarity(LossFunctionWrapper):
    def __init__(self, axis: int = ..., reduction=..., name: str = ...) -> None: ...

bce = binary_crossentropy
BCE = binary_crossentropy
mse = mean_squared_error
MSE = mean_squared_error
mae = mean_absolute_error
MAE = mean_absolute_error
mape = mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error
msle = mean_squared_logarithmic_error
MSLE = mean_squared_logarithmic_error
kld = kl_divergence
KLD = kl_divergence
kullback_leibler_divergence = kl_divergence
logcosh = log_cosh
huber_loss = huber

def is_categorical_crossentropy(loss): ...
def serialize(loss): ...
def deserialize(name, custom_objects: Any | None = ...): ...
def get(identifier): ...

LABEL_DTYPES_FOR_LOSSES: Any

import abc
from abc import abstractmethod
from statsmodels.compat.python import with_metaclass as with_metaclass
from typing import Any

class BaseCrossValidator(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def split(self): ...

class KFold(BaseCrossValidator):
    nobs: Any
    k_folds: Any
    shuffle: Any
    def __init__(self, k_folds, shuffle: bool = ...) -> None: ...
    def split(self, X, y: Any | None = ..., label: Any | None = ...) -> None: ...

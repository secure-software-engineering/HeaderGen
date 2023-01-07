from ..base import BaseEstimator
from abc import ABCMeta, abstractmethod
from typing import Any, List

class _BaseComposition(BaseEstimator, metaclass=ABCMeta):
    steps: List[Any]
    @abstractmethod
    def __init__(self): ...

class _AvailableIfDescriptor:
    fn: Any
    check: Any
    attribute_name: Any
    def __init__(self, fn, check, attribute_name) -> None: ...
    def __get__(self, obj, owner: Any | None = ...): ...

def available_if(check): ...

class _IffHasAttrDescriptor(_AvailableIfDescriptor):
    delegate_names: Any
    def __init__(self, fn, delegate_names, attribute_name) -> None: ...

def if_delegate_has_method(delegate): ...

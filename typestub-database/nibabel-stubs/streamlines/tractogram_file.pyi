import abc
from abc import ABC, abstractmethod

from _typeshed import Incomplete

from .header import Field as Field

class ExtensionWarning(Warning): ...
class HeaderWarning(Warning): ...
class DataWarning(Warning): ...
class HeaderError(Exception): ...
class DataError(Exception): ...

class abstractclassmethod(classmethod):
    __isabstractmethod__: bool
    def __init__(self, callable) -> None: ...

class TractogramFile(ABC, metaclass=abc.ABCMeta):
    def __init__(self, tractogram, header: Incomplete | None = None) -> None: ...
    @property
    def tractogram(self): ...
    @property
    def streamlines(self): ...
    @property
    def header(self): ...
    @property
    def affine(self): ...
    def is_correct_format(cls, fileobj) -> None: ...
    @classmethod
    def create_empty_header(cls): ...
    def load(cls, fileobj, lazy_load: bool = True) -> None: ...
    @abstractmethod
    def save(self, fileobj): ...

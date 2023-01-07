from ctypes import _SimpleCData
from typing import Type

c_intp: Type[_SimpleCData[int]]

def load_library(libname, loader_path) -> None: ...
def ndpointer(dtype=..., ndim=..., shape=..., flags=...) -> None: ...
def as_ctypes(obj) -> None: ...
def as_array(obj, shape=...) -> None: ...
def as_ctypes_type(dtype) -> None: ...

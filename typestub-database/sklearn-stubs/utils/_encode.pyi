from . import is_scalar_nan as is_scalar_nan
from typing import Any, NamedTuple

class MissingValues(NamedTuple):
    nan: bool
    none: bool
    def to_list(self): ...

class _nandict(dict):
    nan_value: Any
    def __init__(self, mapping) -> None: ...
    def __missing__(self, key): ...

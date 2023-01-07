from typing import Any, Optional

def array_like(obj, name, dtype=..., ndim: int = ..., maxdim: Any | None = ..., shape: Any | None = ..., order: Any | None = ..., contiguous: bool = ..., optional: bool = ...): ...

class PandasWrapper:
    def __init__(self, pandas_obj) -> None: ...
    def wrap(self, obj, columns: Any | None = ..., append: Any | None = ..., trim_start: int = ..., trim_end: int = ...): ...

def bool_like(value, name, optional: bool = ..., strict: bool = ...): ...
def int_like(value: Any, name: str, optional: bool = ..., strict: bool = ...) -> Optional[int]: ...
def required_int_like(value: Any, name: str, strict: bool = ...) -> int: ...
def float_like(value, name, optional: bool = ..., strict: bool = ...): ...
def string_like(value, name, optional: bool = ..., options: Any | None = ..., lower: bool = ...): ...
def dict_like(value, name, optional: bool = ..., strict: bool = ...): ...

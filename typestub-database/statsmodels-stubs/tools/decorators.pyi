from statsmodels.compat.pandas import cache_readonly as PandasCacheReadonly
from typing import Any

class ResettableCache(dict):
    __dict__: Any
    def __init__(self, *args, **kwargs) -> None: ...

def deprecated_alias(old_name, new_name, remove_version: Any | None = ..., msg: Any | None = ..., warning=...): ...

class CachedAttribute:
    fget: Any
    name: Any
    cachename: Any
    def __init__(self, func, cachename: Any | None = ...) -> None: ...
    def __get__(self, obj, type: Any | None = ...): ...
    def __set__(self, obj, value) -> None: ...

class CachedWritableAttribute(CachedAttribute):
    def __set__(self, obj, value) -> None: ...

class _cache_readonly(property):
    func: Any
    cachename: Any
    def __init__(self, cachename: Any | None = ...) -> None: ...
    def __call__(self, func): ...

class cache_writable(_cache_readonly):
    def __call__(self, func): ...
cache_readonly = PandasCacheReadonly
cached_data = PandasCacheReadonly
cached_value = PandasCacheReadonly

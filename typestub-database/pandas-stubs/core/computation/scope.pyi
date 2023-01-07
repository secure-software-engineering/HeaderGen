from pandas._libs.tslibs import Timestamp as Timestamp
from pandas.compat.chainmap import DeepChainMap as DeepChainMap
from typing import Union, Any

def ensure_scope(level: int, global_dict: Any | None = ..., local_dict: Any | None = ..., resolvers=..., target: Any | None = ..., **kwargs) -> Scope: ...

DEFAULT_GLOBALS: Any

class Scope:
    level: int
    scope: DeepChainMap
    resolvers: DeepChainMap
    temps: dict
    target: Any
    def __init__(self, level: int, global_dict: Any | None = ..., local_dict: Any | None = ..., resolvers=..., target: Any | None = ...) -> None: ...
    @property
    def has_resolvers(self) -> bool: ...
    def resolve(self, key: str, is_local: bool): ...
    def swapkey(self, old_key: str, new_key: str, new_value: Any | None = ...) -> None: ...
    def add_tmp(self, value) -> str: ...
    @property
    def ntemps(self) -> int: ...
    @property
    def full_scope(self) -> DeepChainMap: ...

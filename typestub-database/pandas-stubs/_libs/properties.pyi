from typing import Union, Any

cache_readonly = property

def __getattr__(name: str) -> Any: ...

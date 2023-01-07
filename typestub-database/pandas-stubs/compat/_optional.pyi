import types
from pandas.util.version import Version as Version
from typing import Union, Any

VERSIONS: Any
INSTALL_MAPPING: Any

def get_version(module: types.ModuleType) -> str: ...
def import_optional_dependency(name: str, extra: str = ..., errors: str = ..., min_version: Union[str, None] = ...): ...

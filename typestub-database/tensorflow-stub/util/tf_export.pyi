from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect
from typing import Any, NamedTuple

ESTIMATOR_API_NAME: str
KERAS_API_NAME: str
TENSORFLOW_API_NAME: str
SUBPACKAGE_NAMESPACES: Any

class _Attributes(NamedTuple):
    names: Any
    constants: Any
API_ATTRS: Any
API_ATTRS_V1: Any

class SymbolAlreadyExposedError(Exception): ...
class InvalidSymbolNameError(Exception): ...

def get_symbol_from_name(name): ...
def get_canonical_name_for_symbol(symbol, api_name=..., add_prefix_to_v1_names: bool = ...): ...
def get_canonical_name(api_names, deprecated_api_names): ...
def get_v1_names(symbol): ...
def get_v2_names(symbol): ...
def get_v1_constants(module): ...
def get_v2_constants(module): ...

class api_export:
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, func): ...
    def set_attr(self, func, api_names_attr, names) -> None: ...
    def export_constant(self, module_name, name) -> None: ...

def kwarg_only(f): ...

tf_export: Any
estimator_export: Any
keras_export: Any

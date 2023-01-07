from numpy.compat._inspect import getargspec as getargspec
from numpy.core._multiarray_umath import add_docstring as add_docstring, implement_array_function as implement_array_function
from typing import Any, NamedTuple

ARRAY_FUNCTION_ENABLED: Any
array_function_like_doc: str

def set_array_function_like_doc(public_api): ...

class ArgSpec(NamedTuple):
    args: Any
    varargs: Any
    keywords: Any
    defaults: Any

def verify_matching_signatures(implementation, dispatcher) -> None: ...
def set_module(module): ...
def array_function_dispatch(dispatcher, module: Any | None = ..., verify: bool = ..., docs_from_dispatcher: bool = ...): ...
def array_function_from_dispatcher(implementation, module: Any | None = ..., verify: bool = ..., docs_from_dispatcher: bool = ...): ...

from contextlib import ContextDecorator
from pandas._typing import F as F
from typing import Union, Any, Callable, Iterable, NamedTuple

class DeprecatedOption(NamedTuple):
    key: str
    msg: Union[str, None]
    rkey: Union[str, None]
    removal_ver: Union[str, None]

class RegisteredOption(NamedTuple):
    key: str
    defval: object
    doc: str
    validator: Union[Callable[[object], Any], None]
    cb: Union[Callable[[str], Any], None]

class OptionError(AttributeError, KeyError): ...

def get_default_val(pat: str): ...

class DictWrapper:
    def __init__(self, d: dict[str, Any], prefix: str = ...) -> None: ...
    def __setattr__(self, key: str, val: Any) -> None: ...
    def __getattr__(self, key: str): ...
    def __dir__(self) -> Iterable[str]: ...

class CallableDynamicDoc:
    __doc_tmpl__: Any
    __func__: Any
    def __init__(self, func, doc_tmpl) -> None: ...
    def __call__(self, *args, **kwds): ...
    @property
    def __doc__(self): ...

get_option: Any
set_option: Any
reset_option: Any
describe_option: Any
options: Any

class option_context(ContextDecorator):
    ops: Any
    def __init__(self, *args) -> None: ...
    undo: Any
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def register_option(key: str, defval: object, doc: str = ..., validator: Union[Callable[[object], Any], None] = ..., cb: Union[Callable[[str], Any], None] = ...) -> None: ...
def deprecate_option(key: str, msg: Union[str, None] = ..., rkey: Union[str, None] = ..., removal_ver: Union[str, None] = ...) -> None: ...
def pp_options_list(keys: Iterable[str], width: int = ..., _print: bool = ...): ...
def config_prefix(prefix): ...
def is_type_factory(_type: type[Any]) -> Callable[[Any], None]: ...
def is_instance_factory(_type) -> Callable[[Any], None]: ...
def is_one_of_factory(legal_values) -> Callable[[Any], None]: ...
def is_nonnegative_int(value: object) -> None: ...

is_int: Any
is_bool: Any
is_float: Any
is_str: Any
is_text: Any

def is_callable(obj) -> bool: ...

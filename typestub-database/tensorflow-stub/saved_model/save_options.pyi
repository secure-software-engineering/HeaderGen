import enum
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class VariablePolicy(enum.Enum):
    NONE: Any
    SAVE_VARIABLE_DEVICES: str
    EXPAND_DISTRIBUTED_VARIABLES: str
    @staticmethod
    def from_obj(obj): ...

class SaveOptions:
    namespace_whitelist: Any
    save_debug_info: Any
    function_aliases: Any
    experimental_custom_gradients: Any
    experimental_io_device: Any
    experimental_variable_policy: Any
    def __init__(self, namespace_whitelist: Any | None = ..., save_debug_info: bool = ..., function_aliases: Any | None = ..., experimental_io_device: Any | None = ..., experimental_variable_policy: Any | None = ..., experimental_custom_gradients: bool = ...) -> None: ...

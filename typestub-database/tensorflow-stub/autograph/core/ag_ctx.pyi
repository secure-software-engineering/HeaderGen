import enum
from tensorflow.python.autograph.utils import ag_logging as ag_logging
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

stacks: Any

def control_status_ctx(): ...

class Status(enum.Enum):
    UNSPECIFIED: int
    ENABLED: int
    DISABLED: int

class ControlStatusCtx:
    status: Any
    options: Any
    def __init__(self, status, options: Any | None = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, unused_type, unused_value, unused_traceback) -> None: ...

class NullCtx:
    def __enter__(self) -> None: ...
    def __exit__(self, unused_type, unused_value, unused_traceback) -> None: ...

INSPECT_SOURCE_SUPPORTED: bool

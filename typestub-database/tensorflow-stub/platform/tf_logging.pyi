from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def get_logger(): ...
def log(level, msg, *args, **kwargs) -> None: ...
def debug(msg, *args, **kwargs) -> None: ...
def error(msg, *args, **kwargs) -> None: ...
def fatal(msg, *args, **kwargs) -> None: ...
def info(msg, *args, **kwargs) -> None: ...
def warn(msg, *args, **kwargs) -> None: ...
def warning(msg, *args, **kwargs) -> None: ...
def TaskLevelStatusMessage(msg) -> None: ...
def flush() -> None: ...
def vlog(level, msg, *args, **kwargs) -> None: ...
def log_every_n(level, msg, n, *args) -> None: ...
def log_first_n(level, msg, n, *args) -> None: ...
def log_if(level, msg, condition, *args) -> None: ...
def google2_log_prefix(level, timestamp: Any | None = ..., file_and_line: Any | None = ...): ...
def get_verbosity(): ...
def set_verbosity(v) -> None: ...

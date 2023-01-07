from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class LoadOptions:
    experimental_io_device: Any
    allow_partial_checkpoint: Any
    experimental_skip_checkpoint: Any
    def __init__(self, allow_partial_checkpoint: bool = ..., experimental_io_device: Any | None = ..., experimental_skip_checkpoint: bool = ...) -> None: ...

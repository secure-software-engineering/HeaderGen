from tensorflow.python.framework import dtypes as dtypes, errors_impl as errors_impl
from tensorflow.python.ops import variables as variables
from tensorflow.python.training import checkpoint_utils as checkpoint_utils
from typing import Any

def list_checkpoint_attributes(ckpt_dir_or_file): ...

class SidecarEvaluator:
    model: Any
    data: Any
    checkpoint_dir: Any
    max_evaluations: Any
    steps: Any
    callbacks: Any
    def __init__(self, model, data, checkpoint_dir, steps: Any | None = ..., max_evaluations: Any | None = ..., callbacks: Any | None = ...) -> None: ...
    def start(self) -> None: ...

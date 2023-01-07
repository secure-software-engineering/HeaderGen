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

class SidecarEvaluatorExperimental(SidecarEvaluator):
    def __init__(self, *args, **kwargs) -> None: ...

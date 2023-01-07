from typing import Any

class DatasetCreator:
    dataset_fn: Any
    input_options: Any
    def __init__(self, dataset_fn, input_options: Any | None = ...) -> None: ...
    def __call__(self, *args, **kwargs): ...

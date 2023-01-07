from typing import Any

class StandardizeTransform:
    mean: Any
    scale: Any
    const_idx: Any
    def __init__(self, data, ddof: int = ..., const_idx: Any | None = ..., demean: bool = ...) -> None: ...
    def transform(self, data): ...
    def transform_params(self, params): ...
    __call__: Any

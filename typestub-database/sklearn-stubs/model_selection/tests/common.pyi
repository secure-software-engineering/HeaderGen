from sklearn.model_selection import KFold as KFold
from typing import Any

class OneTimeSplitter:
    n_splits: Any
    n_samples: Any
    indices: Any
    def __init__(self, n_splits: int = ..., n_samples: int = ...) -> None: ...
    def split(self, X: Any | None = ..., y: Any | None = ..., groups: Any | None = ...) -> None: ...
    def get_n_splits(self, X: Any | None = ..., y: Any | None = ..., groups: Any | None = ...): ...

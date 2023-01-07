from ..utils import gen_batches as gen_batches
from ..utils.extmath import svd_flip as svd_flip
from ._base import _BasePCA
from typing import Any

class IncrementalPCA(_BasePCA):
    n_components: Any
    whiten: Any
    copy: Any
    batch_size: Any
    def __init__(self, n_components: Any | None = ..., *, whiten: bool = ..., copy: bool = ..., batch_size: Any | None = ...) -> None: ...
    components_: Any
    n_samples_seen_: int
    mean_: float
    var_: float
    singular_values_: Any
    explained_variance_: Any
    explained_variance_ratio_: Any
    noise_variance_: Any
    batch_size_: Any
    def fit(self, X, y: Any | None = ...): ...
    n_components_: Any
    def partial_fit(self, X, y: Any | None = ..., check_input: bool = ...): ...
    def transform(self, X): ...

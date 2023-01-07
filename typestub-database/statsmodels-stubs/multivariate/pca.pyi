from statsmodels.tools.sm_exceptions import EstimationWarning as EstimationWarning, ValueWarning as ValueWarning
from statsmodels.tools.validation import array_like as array_like, bool_like as bool_like, float_like as float_like, int_like as int_like, string_like as string_like
from typing import Any

class PCA:
    data: Any
    weights: Any
    rows: Any
    cols: Any
    transformed_data: Any
    scores: Any
    loadings: Any
    coeff: Any
    eigenvals: Any
    eigenvecs: Any
    projection: Any
    rsquare: Any
    ic: Any
    def __init__(self, data, ncomp: Any | None = ..., standardize: bool = ..., demean: bool = ..., normalize: bool = ..., gls: bool = ..., weights: Any | None = ..., method: str = ..., missing: Any | None = ..., tol: float = ..., max_iter: int = ..., tol_em: float = ..., max_em_iter: int = ..., svd_full_matrices: bool = ...) -> None: ...
    def project(self, ncomp: Any | None = ..., transform: bool = ..., unweight: bool = ...): ...
    def plot_scree(self, ncomp: Any | None = ..., log_scale: bool = ..., cumulative: bool = ..., ax: Any | None = ...): ...
    def plot_rsquare(self, ncomp: Any | None = ..., ax: Any | None = ...): ...

def pca(data, ncomp: Any | None = ..., standardize: bool = ..., demean: bool = ..., normalize: bool = ..., gls: bool = ..., weights: Any | None = ..., method: str = ...): ...

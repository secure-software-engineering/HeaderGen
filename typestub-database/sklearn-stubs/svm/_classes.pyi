from ..base import BaseEstimator as BaseEstimator, OutlierMixin as OutlierMixin, RegressorMixin as RegressorMixin
from ..linear_model._base import LinearClassifierMixin as LinearClassifierMixin, LinearModel as LinearModel, SparseCoefMixin as SparseCoefMixin
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ._base import BaseLibSVM as BaseLibSVM, BaseSVC as BaseSVC
from typing import Any

class LinearSVC(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    dual: Any
    tol: Any
    C: Any
    multi_class: Any
    fit_intercept: Any
    intercept_scaling: Any
    class_weight: Any
    verbose: Any
    random_state: Any
    max_iter: Any
    penalty: Any
    loss: Any
    def __init__(self, penalty: str = ..., loss: str = ..., *, dual: bool = ..., tol: float = ..., C: float = ..., multi_class: str = ..., fit_intercept: bool = ..., intercept_scaling: int = ..., class_weight: Any | None = ..., verbose: int = ..., random_state: Any | None = ..., max_iter: int = ...) -> None: ...
    classes_: Any
    coef_: Any
    intercept_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class LinearSVR(RegressorMixin, LinearModel):
    tol: Any
    C: Any
    epsilon: Any
    fit_intercept: Any
    intercept_scaling: Any
    verbose: Any
    random_state: Any
    max_iter: Any
    dual: Any
    loss: Any
    def __init__(self, *, epsilon: float = ..., tol: float = ..., C: float = ..., loss: str = ..., fit_intercept: bool = ..., intercept_scaling: float = ..., dual: bool = ..., verbose: int = ..., random_state: Any | None = ..., max_iter: int = ...) -> None: ...
    coef_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class SVC(BaseSVC):
    def __init__(self, *, C: float = ..., kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., shrinking: bool = ..., probability: bool = ..., tol: float = ..., cache_size: int = ..., class_weight: Any | None = ..., verbose: bool = ..., max_iter: int = ..., decision_function_shape: str = ..., break_ties: bool = ..., random_state: Any | None = ...) -> None: ...

class NuSVC(BaseSVC):
    def __init__(self, *, nu: float = ..., kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., shrinking: bool = ..., probability: bool = ..., tol: float = ..., cache_size: int = ..., class_weight: Any | None = ..., verbose: bool = ..., max_iter: int = ..., decision_function_shape: str = ..., break_ties: bool = ..., random_state: Any | None = ...) -> None: ...

class SVR(RegressorMixin, BaseLibSVM):
    def __init__(self, *, kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., tol: float = ..., C: float = ..., epsilon: float = ..., shrinking: bool = ..., cache_size: int = ..., verbose: bool = ..., max_iter: int = ...) -> None: ...

class NuSVR(RegressorMixin, BaseLibSVM):
    def __init__(self, *, nu: float = ..., C: float = ..., kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., shrinking: bool = ..., tol: float = ..., cache_size: int = ..., verbose: bool = ..., max_iter: int = ...) -> None: ...

class OneClassSVM(OutlierMixin, BaseLibSVM):
    def __init__(self, *, kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., tol: float = ..., nu: float = ..., shrinking: bool = ..., cache_size: int = ..., verbose: bool = ..., max_iter: int = ...) -> None: ...
    offset_: Any
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ..., **params): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def predict(self, X): ...

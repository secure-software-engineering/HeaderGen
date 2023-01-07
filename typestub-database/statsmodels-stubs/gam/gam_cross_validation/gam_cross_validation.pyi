import abc
from statsmodels.compat.python import with_metaclass as with_metaclass
from statsmodels.gam.smooth_basis import GenericSmoothers as GenericSmoothers, UnivariateGenericSmoother as UnivariateGenericSmoother
from typing import Any

class BaseCV(metaclass=abc.ABCMeta):
    cv_iterator: Any
    exog: Any
    endog: Any
    train_test_cv_indices: Any
    def __init__(self, cv_iterator, endog, exog) -> None: ...
    def fit(self, **kwargs): ...

class MultivariateGAMCV(BaseCV):
    cost: Any
    gam: Any
    smoother: Any
    exog_linear: Any
    alphas: Any
    cv_iterator: Any
    def __init__(self, smoother, alphas, gam, cost, endog, exog, cv_iterator) -> None: ...

class BasePenaltiesPathCV:
    alphas: Any
    alpha_cv: Any
    cv_error: Any
    cv_std: Any
    def __init__(self, alphas) -> None: ...
    def plot_path(self) -> None: ...

class MultivariateGAMCVPath:
    cost: Any
    smoother: Any
    gam: Any
    alphas: Any
    alphas_grid: Any
    endog: Any
    exog: Any
    cv_iterator: Any
    cv_error: Any
    cv_std: Any
    alpha_cv: Any
    def __init__(self, smoother, alphas, gam, cost, endog, exog, cv_iterator) -> None: ...
    def fit(self, **kwargs): ...

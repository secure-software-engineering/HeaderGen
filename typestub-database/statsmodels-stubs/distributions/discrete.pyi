from scipy.stats import rv_discrete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel
from typing import Any

class genpoisson_p_gen(rv_discrete): ...

genpoisson_p: Any

class zipoisson_gen(rv_discrete): ...

zipoisson: Any

class zigeneralizedpoisson_gen(rv_discrete): ...

zigenpoisson: Any

class zinegativebinomial_gen(rv_discrete):
    def convert_params(self, mu, alpha, p): ...

zinegbin: Any

class DiscretizedCount(rv_discrete):
    def __new__(cls, *args, **kwds): ...
    distr: Any
    d_offset: Any
    add_scale: Any
    k_shapes: Any
    def __init__(self, distr, d_offset: int = ..., add_scale: bool = ..., **kwds) -> None: ...

class DiscretizedModel(GenericLikelihoodModel):
    df_resid: Any
    df_model: Any
    k_constant: int
    nparams: Any
    start_params: Any
    def __init__(self, endog, exog: Any | None = ..., distr: Any | None = ...) -> None: ...
    def loglike(self, params): ...
    def predict(self, params, exog: Any | None = ..., which: Any | None = ..., k_max: int = ...): ...
    def get_distr(self, params): ...

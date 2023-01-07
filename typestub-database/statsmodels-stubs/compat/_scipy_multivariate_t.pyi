from typing import Any

class _PSD:
    rank: Any
    U: Any
    log_pdet: Any
    def __init__(self, M, cond: Any | None = ..., rcond: Any | None = ..., lower: bool = ..., check_finite: bool = ..., allow_singular: bool = ...) -> None: ...
    @property
    def pinv(self): ...

class multi_rv_generic:
    def __init__(self, seed: Any | None = ...) -> None: ...
    @property
    def random_state(self): ...
    @random_state.setter
    def random_state(self, seed) -> None: ...

class multi_rv_frozen:
    @property
    def random_state(self): ...
    @random_state.setter
    def random_state(self, seed) -> None: ...

mvn_docdict_params: Any
mvn_docdict_noparams: Any

class multivariate_normal_gen(multi_rv_generic):
    __doc__: Any
    def __init__(self, seed: Any | None = ...) -> None: ...
    def __call__(self, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ..., seed: Any | None = ...): ...
    def logpdf(self, x, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ...): ...
    def pdf(self, x, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ...): ...
    def logcdf(self, x, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ..., maxpts: Any | None = ..., abseps: float = ..., releps: float = ...): ...
    def cdf(self, x, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ..., maxpts: Any | None = ..., abseps: float = ..., releps: float = ...): ...
    def rvs(self, mean: Any | None = ..., cov: int = ..., size: int = ..., random_state: Any | None = ...): ...
    def entropy(self, mean: Any | None = ..., cov: int = ...): ...

multivariate_normal: Any

class multivariate_normal_frozen(multi_rv_frozen):
    cov_info: Any
    maxpts: Any
    abseps: Any
    releps: Any
    def __init__(self, mean: Any | None = ..., cov: int = ..., allow_singular: bool = ..., seed: Any | None = ..., maxpts: Any | None = ..., abseps: float = ..., releps: float = ...) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def logcdf(self, x): ...
    def cdf(self, x): ...
    def rvs(self, size: int = ..., random_state: Any | None = ...): ...
    def entropy(self): ...

mvt_docdict_params: Any
mvt_docdict_noparams: Any

class multivariate_t_gen(multi_rv_generic):
    __doc__: Any
    def __init__(self, seed: Any | None = ...) -> None: ...
    def __call__(self, loc: Any | None = ..., shape: int = ..., df: int = ..., allow_singular: bool = ..., seed: Any | None = ...): ...
    def pdf(self, x, loc: Any | None = ..., shape: int = ..., df: int = ..., allow_singular: bool = ...): ...
    def logpdf(self, x, loc: Any | None = ..., shape: int = ..., df: int = ...): ...
    def rvs(self, loc: Any | None = ..., shape: int = ..., df: int = ..., size: int = ..., random_state: Any | None = ...): ...

class multivariate_t_frozen(multi_rv_frozen):
    shape_info: Any
    def __init__(self, loc: Any | None = ..., shape: int = ..., df: int = ..., allow_singular: bool = ..., seed: Any | None = ...) -> None: ...
    def logpdf(self, x): ...
    def pdf(self, x): ...
    def rvs(self, size: int = ..., random_state: Any | None = ...): ...

multivariate_t: Any
method: Any
method_frozen: Any

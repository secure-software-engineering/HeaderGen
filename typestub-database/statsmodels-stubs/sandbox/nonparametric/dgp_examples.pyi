from typing import Any

def fg1(x): ...
def fg1eu(x): ...
def fg2(x): ...
def func1(x): ...

doc: Any

class _UnivariateFunction:
    __doc__: str
    x: Any
    y_true: Any
    y: Any
    def __init__(self, nobs: int = ..., x: Any | None = ..., distr_x: Any | None = ..., distr_noise: Any | None = ...) -> None: ...
    def plot(self, scatter: bool = ..., ax: Any | None = ...): ...

class UnivariateFanGijbels1(_UnivariateFunction):
    __doc__: Any
    s_x: float
    s_noise: float
    func: Any
    def __init__(self, nobs: int = ..., x: Any | None = ..., distr_x: Any | None = ..., distr_noise: Any | None = ...) -> None: ...

class UnivariateFanGijbels2(_UnivariateFunction):
    __doc__: Any
    s_x: float
    s_noise: float
    func: Any
    def __init__(self, nobs: int = ..., x: Any | None = ..., distr_x: Any | None = ..., distr_noise: Any | None = ...) -> None: ...

class UnivariateFanGijbels1EU(_UnivariateFunction):
    s_noise: float
    func: Any
    def __init__(self, nobs: int = ..., x: Any | None = ..., distr_x: Any | None = ..., distr_noise: Any | None = ...) -> None: ...

class UnivariateFunc1(_UnivariateFunction):
    s_noise: float
    func: Any
    def __init__(self, nobs: int = ..., x: Any | None = ..., distr_x: Any | None = ..., distr_noise: Any | None = ...) -> None: ...
    def het_scale(self, x): ...

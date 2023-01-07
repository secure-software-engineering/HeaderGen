from . import kernels as kernels
from typing import Any

has_joblib: bool
kernel_func: Any

class GenericKDE:
    def loo_likelihood(self) -> None: ...

class EstimatorSettings:
    efficient: Any
    randomize: Any
    n_res: Any
    n_sub: Any
    return_median: Any
    return_only_bw: Any
    n_jobs: Any
    def __init__(self, efficient: bool = ..., randomize: bool = ..., n_res: int = ..., n_sub: int = ..., return_median: bool = ..., return_only_bw: bool = ..., n_jobs: int = ...) -> None: ...

class LeaveOneOut:
    X: Any
    def __init__(self, X) -> None: ...
    def __iter__(self): ...

def gpke(bw, data, data_predict, var_type, ckertype: str = ..., okertype: str = ..., ukertype: str = ..., tosum: bool = ...): ...

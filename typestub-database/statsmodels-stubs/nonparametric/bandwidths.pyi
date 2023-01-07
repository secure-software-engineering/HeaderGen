from statsmodels.compat.pandas import Substitution as Substitution
from statsmodels.sandbox.nonparametric import kernels as kernels
from typing import Any

def bw_scott(x, kernel: Any | None = ...): ...
def bw_silverman(x, kernel: Any | None = ...): ...
def bw_normal_reference(x, kernel: Any | None = ...): ...

bandwidth_funcs: Any

def select_bandwidth(x, bw, kernel): ...

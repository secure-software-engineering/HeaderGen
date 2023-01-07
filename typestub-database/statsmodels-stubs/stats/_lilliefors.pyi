from ._lilliefors_critical_values import PERCENTILES as PERCENTILES, asymp_critical_values as asymp_critical_values, critical_values as critical_values
from .tabledist import TableDist as TableDist
from statsmodels.tools.validation import string_like as string_like
from typing import Any

def ksstat(x, cdf, alternative: str = ..., args=...): ...
def get_lilliefors_table(dist: str = ...): ...

lilliefors_table_norm: Any
lilliefors_table_expon: Any

def pval_lf(d_max, n): ...
def kstest_fit(x, dist: str = ..., pvalmethod: str = ...): ...
lilliefors = kstest_fit
kstest_normal = kstest_fit
kstest_exponential: Any

from statsmodels.stats.multitest import multipletests as multipletests
from statsmodels.tools.tools import clean0 as clean0, fullrank as fullrank
from typing import Any

class ContrastResults:
    effect: Any
    distribution: str
    fvalue: Any
    statistic: Any
    df_denom: Any
    df_num: Any
    dist: Any
    dist_args: Any
    pvalue: Any
    tvalue: Any
    sd: Any
    def __init__(self, t: Any | None = ..., F: Any | None = ..., sd: Any | None = ..., effect: Any | None = ..., df_denom: Any | None = ..., df_num: Any | None = ..., alpha: float = ..., **kwds) -> None: ...
    def conf_int(self, alpha: float = ...): ...
    def summary(self, xname: Any | None = ..., alpha: float = ..., title: Any | None = ...): ...
    def summary_frame(self, xname: Any | None = ..., alpha: float = ...): ...

class Contrast:
    contrast_matrix: Any
    term: Any
    design: Any
    def __init__(self, term, design) -> None: ...
    T: Any
    D: Any
    rank: Any
    def compute_matrix(self) -> None: ...

def contrastfromcols(L, D, pseudo: Any | None = ...): ...

class WaldTestResults:
    table: Any
    distribution: Any
    statistic: Any
    dist_args: Any
    pvalues: Any
    df_constraints: Any
    df_denom: Any
    dist: Any
    def __init__(self, statistic, distribution, dist_args, table: Any | None = ..., pvalues: Any | None = ...) -> None: ...
    @property
    def col_names(self): ...
    dframe: Any
    def summary_frame(self): ...

def t_test_multi(result, contrasts, method: str = ..., alpha: float = ..., ci_method: Any | None = ..., contrast_names: Any | None = ...): ...

class MultiCompResult:
    def __init__(self, **kwargs) -> None: ...

def t_test_pairwise(result, term_name, method: str = ..., alpha: float = ..., factor_labels: Any | None = ..., ignore: bool = ...): ...
def wald_test_noncent(params, r_matrix, value, results, diff: Any | None = ..., joint: bool = ...): ...
def wald_test_noncent_generic(params, r_matrix, value, cov_params, diff: Any | None = ..., joint: bool = ...): ...

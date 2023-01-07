import numpy as np
from statsmodels.compat.python import lzip as lzip
from statsmodels.iolib import SimpleTable as SimpleTable
from typing import Any

mat = np.array

class VARSummary:
    default_fmt: Any
    part1_fmt: Any
    part2_fmt: Any
    model: Any
    summary: Any
    def __init__(self, estimator) -> None: ...
    def make(self, endog_names: Any | None = ..., exog_names: Any | None = ...): ...

def normality_summary(results): ...
def hypothesis_test_table(results, title, null_hyp): ...
def pprint_matrix(values, rlabels, clabels, col_space: Any | None = ...): ...

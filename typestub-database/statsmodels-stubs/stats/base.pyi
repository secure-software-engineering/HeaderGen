from statsmodels.compat.python import lzip as lzip
from statsmodels.tools.testing import Holder as Holder
from typing import Any

class HolderTuple(Holder):
    tuple: Any
    def __init__(self, tuple_: Any | None = ..., **kwds) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, idx): ...
    def __len__(self): ...
    def __array__(self, dtype: Any | None = ...): ...

class AllPairsResults:
    pvals_raw: Any
    all_pairs: Any
    n_levels: Any
    multitest_method: Any
    levels: Any
    all_pairs_names: Any
    def __init__(self, pvals_raw, all_pairs, multitest_method: str = ..., levels: Any | None = ..., n_levels: Any | None = ...) -> None: ...
    def pval_corrected(self, method: Any | None = ...): ...
    def pval_table(self): ...
    def summary(self): ...

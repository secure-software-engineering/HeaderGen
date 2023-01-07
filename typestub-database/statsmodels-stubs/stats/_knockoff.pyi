from statsmodels.iolib import summary2 as summary2
from typing import Any

class RegressionFDR:
    xnames: Any
    endog: Any
    exog: Any
    exog1: Any
    exog2: Any
    stats: Any
    fdr: Any
    fdrp: Any
    fdr_df: Any
    def __init__(self, endog, exog, regeffects, method: str = ..., **kwargs) -> None: ...
    def threshold(self, tfdr): ...
    def summary(self): ...

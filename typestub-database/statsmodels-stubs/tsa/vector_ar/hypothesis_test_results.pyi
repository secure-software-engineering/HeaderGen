from statsmodels.iolib.table import SimpleTable as SimpleTable
from typing import Any

class HypothesisTestResults:
    test_statistic: Any
    crit_value: Any
    pvalue: Any
    df: Any
    signif: Any
    method: Any
    conclusion: str
    title: Any
    h0: Any
    conclusion_str: Any
    signif_str: Any
    def __init__(self, test_statistic, crit_value, pvalue, df, signif, method, title, h0) -> None: ...
    def summary(self): ...
    def __eq__(self, other): ...

class CausalityTestResults(HypothesisTestResults):
    causing: Any
    caused: Any
    test: Any
    def __init__(self, causing, caused, test_statistic, crit_value, pvalue, df, signif, test: str = ..., method: Any | None = ...) -> None: ...
    def __eq__(self, other): ...

class NormalityTestResults(HypothesisTestResults):
    def __init__(self, test_statistic, crit_value, pvalue, df, signif) -> None: ...

class WhitenessTestResults(HypothesisTestResults):
    lags: Any
    adjusted: Any
    def __init__(self, test_statistic, crit_value, pvalue, df, signif, nlags, adjusted) -> None: ...

from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning

def durbin_watson(resids, axis: int = ...): ...
def omni_normtest(resids, axis: int = ...): ...
def jarque_bera(resids, axis: int = ...): ...
def robust_skewness(y, axis: int = ...): ...
def expected_robust_kurtosis(ab=..., dg=...): ...
def robust_kurtosis(y, axis: int = ..., ab=..., dg=..., excess: bool = ...): ...
def medcouple(y, axis: int = ...): ...

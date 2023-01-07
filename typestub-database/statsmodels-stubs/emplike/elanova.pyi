from .descriptive import _OptFuncts
from typing import Any

class _ANOVAOpt(_OptFuncts): ...

class ANOVA(_ANOVAOpt):
    endog: Any
    num_groups: Any
    nobs: int
    def __init__(self, endog) -> None: ...
    def compute_ANOVA(self, mu: Any | None = ..., mu_start: int = ..., return_weights: int = ...): ...

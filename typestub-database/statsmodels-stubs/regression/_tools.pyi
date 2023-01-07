from statsmodels.tools.tools import Bunch as Bunch
from typing import Any

class _MinimalWLS:
    msg: str
    endog: Any
    exog: Any
    weights: Any
    wendog: Any
    wexog: Any
    def __init__(self, endog, exog, weights: float = ..., check_endog: bool = ..., check_weights: bool = ...) -> None: ...
    def fit(self, method: str = ...): ...
    def results(self, params): ...

from statsmodels.regression.linear_model import OLS as OLS, WLS as WLS
from typing import Any

class OneWayLS:
    endog: Any
    exog: Any
    groups: Any
    het: Any
    groupsint: Any
    unique: Any
    uniqueint: Any
    def __init__(self, y, x, groups: Any | None = ..., het: bool = ..., data: Any | None = ..., meta: Any | None = ...) -> None: ...
    olsbygroup: Any
    sigmabygroup: Any
    weights: Any
    def fitbygroups(self) -> None: ...
    lsjoint: Any
    contrasts: Any
    def fitjoint(self) -> None: ...
    lspooled: Any
    def fitpooled(self) -> None: ...
    summarytable: Any
    def ftest_summary(self): ...
    def print_summary(self, res): ...
    def lr_test(self): ...

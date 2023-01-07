from statsmodels.base._penalties import SCADSmoothed as SCADSmoothed
from typing import Any

class ScreeningResults:
    screener: Any
    def __init__(self, screener, **kwds) -> None: ...

class VariableScreening:
    model: Any
    model_class: Any
    init_kwds: Any
    endog: Any
    exog_keep: Any
    k_keep: Any
    nobs: Any
    penal: Any
    pen_weight: Any
    use_weights: Any
    k_add: Any
    k_max_add: Any
    threshold_trim: Any
    k_max_included: Any
    ranking_attr: Any
    ranking_project: Any
    def __init__(self, model, pen_weight: Any | None = ..., use_weights: bool = ..., k_add: int = ..., k_max_add: int = ..., threshold_trim: float = ..., k_max_included: int = ..., ranking_attr: str = ..., ranking_project: bool = ...) -> None: ...
    def ranking_measure(self, res_pen, exog, keep: Any | None = ...): ...
    def screen_exog(self, exog, endog: Any | None = ..., maxiter: int = ..., method: str = ..., disp: bool = ..., fit_kwds: Any | None = ...): ...
    def screen_exog_iterator(self, exog_iterator): ...

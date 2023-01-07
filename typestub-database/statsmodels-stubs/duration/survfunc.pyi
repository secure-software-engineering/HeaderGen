from statsmodels.graphics import utils as utils
from typing import Any

class CumIncidenceRight:
    times: Any
    cinc: Any
    cinc_se: Any
    title: Any
    def __init__(self, time, status, title: Any | None = ..., freq_weights: Any | None = ..., exog: Any | None = ..., bw_factor: float = ..., dimred: bool = ...): ...

class SurvfuncRight:
    surv_prob: Any
    surv_times: Any
    surv_prob_se: Any
    n_risk: Any
    n_events: Any
    title: Any
    def __init__(self, time, status, entry: Any | None = ..., title: Any | None = ..., freq_weights: Any | None = ..., exog: Any | None = ..., bw_factor: float = ...): ...
    def plot(self, ax: Any | None = ...): ...
    def quantile(self, p): ...
    def quantile_ci(self, p, alpha: float = ..., method: str = ...): ...
    def summary(self): ...
    def simultaneous_cb(self, alpha: float = ..., method: str = ..., transform: str = ...): ...

def survdiff(time, status, group, weight_type: Any | None = ..., strata: Any | None = ..., entry: Any | None = ..., **kwargs): ...
def plot_survfunc(survfuncs, ax: Any | None = ...): ...

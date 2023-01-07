from typing import Any

class PredictionResults:
    predicted_mean: Any
    var_pred_mean: Any
    df: Any
    var_resid: Any
    row_labels: Any
    dist: Any
    dist_args: Any
    def __init__(self, predicted_mean, var_pred_mean, var_resid, df: Any | None = ..., dist: Any | None = ..., row_labels: Any | None = ...) -> None: ...
    @property
    def se_obs(self): ...
    @property
    def se_mean(self): ...
    def conf_int(self, obs: bool = ..., alpha: float = ...): ...
    table: Any
    def summary_frame(self, alpha: float = ...): ...

def get_prediction(self, exog: Any | None = ..., transform: bool = ..., weights: Any | None = ..., row_labels: Any | None = ..., pred_kwds: Any | None = ...): ...

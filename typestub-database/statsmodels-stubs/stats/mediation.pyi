from statsmodels.graphics.utils import maybe_name_or_idx as maybe_name_or_idx
from typing import Any

class Mediation:
    outcome_model: Any
    mediator_model: Any
    exposure: Any
    moderators: Any
    mediator: Any
    def __init__(self, outcome_model, mediator_model, exposure, mediator: Any | None = ..., moderators: Any | None = ..., outcome_fit_kwargs: Any | None = ..., mediator_fit_kwargs: Any | None = ..., outcome_predict_kwargs: Any | None = ...) -> None: ...
    indirect_effects: Any
    direct_effects: Any
    def fit(self, method: str = ..., n_rep: int = ...): ...

class MediationResults:
    indirect_effects: Any
    direct_effects: Any
    ACME_ctrl: Any
    ACME_tx: Any
    ADE_ctrl: Any
    ADE_tx: Any
    total_effect: Any
    prop_med_ctrl: Any
    prop_med_tx: Any
    prop_med_avg: Any
    ACME_avg: Any
    ADE_avg: Any
    def __init__(self, indirect_effects, direct_effects) -> None: ...
    def summary(self, alpha: float = ...): ...

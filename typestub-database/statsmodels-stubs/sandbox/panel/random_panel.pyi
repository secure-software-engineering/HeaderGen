from typing import Any

class PanelSample:
    nobs: Any
    nobs_i: Any
    n_groups: Any
    k_vars: Any
    corr_structure: Any
    groups: Any
    group_indices: Any
    exog: Any
    y_true: Any
    beta: Any
    seed: Any
    random_state: Any
    std: Any
    cov: Any
    group_means: Any
    def __init__(self, nobs, k_vars, n_groups, exog: Any | None = ..., within: bool = ..., corr_structure=..., corr_args=..., scale: int = ..., seed: Any | None = ...) -> None: ...
    def get_y_true(self) -> None: ...
    def generate_panel(self): ...

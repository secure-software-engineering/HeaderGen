from .. import partial_dependence as partial_dependence
from ...base import is_regressor as is_regressor
from ...utils import check_array as check_array, check_matplotlib_support as check_matplotlib_support, check_random_state as check_random_state, deprecated as deprecated
from ...utils.fixes import delayed as delayed
from typing import Any

def plot_partial_dependence(estimator, X, features, *, feature_names: Any | None = ..., target: Any | None = ..., response_method: str = ..., n_cols: int = ..., grid_resolution: int = ..., percentiles=..., method: str = ..., n_jobs: Any | None = ..., verbose: int = ..., line_kw: Any | None = ..., ice_lines_kw: Any | None = ..., pd_line_kw: Any | None = ..., contour_kw: Any | None = ..., ax: Any | None = ..., kind: str = ..., subsample: int = ..., random_state: Any | None = ...): ...

class PartialDependenceDisplay:
    pd_results: Any
    features: Any
    feature_names: Any
    target_idx: Any
    pdp_lim: Any
    deciles: Any
    kind: Any
    subsample: Any
    random_state: Any
    def __init__(self, pd_results, features, feature_names, target_idx, pdp_lim, deciles, *, kind: str = ..., subsample: int = ..., random_state: Any | None = ...) -> None: ...
    @classmethod
    def from_estimator(cls, estimator, X, features, *, feature_names: Any | None = ..., target: Any | None = ..., response_method: str = ..., n_cols: int = ..., grid_resolution: int = ..., percentiles=..., method: str = ..., n_jobs: Any | None = ..., verbose: int = ..., line_kw: Any | None = ..., ice_lines_kw: Any | None = ..., pd_line_kw: Any | None = ..., contour_kw: Any | None = ..., ax: Any | None = ..., kind: str = ..., subsample: int = ..., random_state: Any | None = ...): ...
    bounding_ax_: Any
    figure_: Any
    axes_: Any
    lines_: Any
    contours_: Any
    deciles_vlines_: Any
    deciles_hlines_: Any
    def plot(self, *, ax: Any | None = ..., n_cols: int = ..., line_kw: Any | None = ..., ice_lines_kw: Any | None = ..., pd_line_kw: Any | None = ..., contour_kw: Any | None = ...): ...

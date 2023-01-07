from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_array as check_array
from ..utils.extmath import row_norms as row_norms
from ._base import make_dataset as make_dataset
from ._sag_fast import sag32 as sag32, sag64 as sag64
from typing import Any

def get_auto_step_size(max_squared_sum, alpha_scaled, loss, fit_intercept, n_samples: Any | None = ..., is_saga: bool = ...): ...
def sag_solver(X, y, sample_weight: Any | None = ..., loss: str = ..., alpha: float = ..., beta: float = ..., max_iter: int = ..., tol: float = ..., verbose: int = ..., random_state: Any | None = ..., check_input: bool = ..., max_squared_sum: Any | None = ..., warm_start_mem: Any | None = ..., is_saga: bool = ...): ...

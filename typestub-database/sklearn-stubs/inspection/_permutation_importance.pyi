from ..metrics import check_scoring as check_scoring
from ..utils import Bunch as Bunch, check_array as check_array, check_random_state as check_random_state
from ..utils.fixes import delayed as delayed
from typing import Any

def permutation_importance(estimator, X, y, *, scoring: Any | None = ..., n_repeats: int = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., sample_weight: Any | None = ..., max_samples: float = ...): ...

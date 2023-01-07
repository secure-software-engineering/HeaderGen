from typing import Any

SMOOTHER_STATE: int
SMOOTHER_STATE_COV: int
SMOOTHER_DISTURBANCE: int
SMOOTHER_DISTURBANCE_COV: int
SMOOTHER_ALL: Any

class _KalmanSmoother:
    model: Any
    kfilter: Any
    smoother_output: Any
    scaled_smoothed_estimator: Any
    scaled_smoothed_estimator_cov: Any
    smoothing_error: Any
    smoothed_state: Any
    smoothed_state_cov: Any
    smoothed_state_disturbance: Any
    smoothed_state_disturbance_cov: Any
    smoothed_measurement_disturbance: Any
    smoothed_measurement_disturbance_cov: Any
    tmp_L: Any
    def __init__(self, model, kfilter, smoother_output) -> None: ...
    t: Any
    def seek(self, t) -> None: ...
    def __iter__(self): ...
    def __call__(self) -> None: ...
    def next(self): ...
    def __next__(self) -> None: ...

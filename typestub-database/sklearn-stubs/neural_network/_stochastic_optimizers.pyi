from typing import Any

class BaseOptimizer:
    learning_rate_init: Any
    learning_rate: Any
    def __init__(self, learning_rate_init: float = ...) -> None: ...
    def update_params(self, params, grads) -> None: ...
    def iteration_ends(self, time_step) -> None: ...
    def trigger_stopping(self, msg, verbose): ...

class SGDOptimizer(BaseOptimizer):
    lr_schedule: Any
    momentum: Any
    nesterov: Any
    power_t: Any
    velocities: Any
    def __init__(self, params, learning_rate_init: float = ..., lr_schedule: str = ..., momentum: float = ..., nesterov: bool = ..., power_t: float = ...) -> None: ...
    learning_rate: Any
    def iteration_ends(self, time_step) -> None: ...
    def trigger_stopping(self, msg, verbose): ...

class AdamOptimizer(BaseOptimizer):
    beta_1: Any
    beta_2: Any
    epsilon: Any
    t: int
    ms: Any
    vs: Any
    def __init__(self, params, learning_rate_init: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ...) -> None: ...

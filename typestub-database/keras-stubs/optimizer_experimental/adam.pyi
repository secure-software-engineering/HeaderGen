from keras.optimizer_experimental import optimizer as optimizer
from keras.utils import generic_utils as generic_utils
from typing import Any

class Adam(optimizer.Optimizer):
    beta_1: Any
    beta_2: Any
    epsilon: Any
    amsgrad: Any
    def __init__(self, learning_rate: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., amsgrad: bool = ..., clipnorm: Any | None = ..., clipvalue: Any | None = ..., global_clipnorm: Any | None = ..., use_ema: bool = ..., ema_momentum: float = ..., ema_overwrite_frequency: int = ..., jit_compile: bool = ..., name: str = ..., **kwargs) -> None: ...
    def build(self, var_list) -> None: ...
    def update_step(self, gradient, variable) -> None: ...
    def get_config(self): ...

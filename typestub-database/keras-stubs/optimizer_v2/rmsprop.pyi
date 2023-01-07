from keras import backend_config as backend_config
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from typing import Any

class RMSprop(optimizer_v2.OptimizerV2):
    epsilon: Any
    centered: Any
    def __init__(self, learning_rate: float = ..., rho: float = ..., momentum: float = ..., epsilon: float = ..., centered: bool = ..., name: str = ..., **kwargs) -> None: ...
    def set_weights(self, weights) -> None: ...
    def get_config(self): ...
RMSProp = RMSprop

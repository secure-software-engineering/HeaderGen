from keras import backend_config as backend_config
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from typing import Any

class Adamax(optimizer_v2.OptimizerV2):
    epsilon: Any
    def __init__(self, learning_rate: float = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., name: str = ..., **kwargs) -> None: ...
    def get_config(self): ...

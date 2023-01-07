from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from typing import Any

class SGD(optimizer_v2.OptimizerV2):
    nesterov: Any
    def __init__(self, learning_rate: float = ..., momentum: float = ..., nesterov: bool = ..., name: str = ..., **kwargs) -> None: ...
    def get_config(self): ...

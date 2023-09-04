from typing import Any

from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.src.layers.core.dropout import Dropout as Dropout

class SpatialDropout1D(Dropout):
    input_spec: Any
    def __init__(self, rate, **kwargs) -> None: ...

class SpatialDropout2D(Dropout):
    data_format: Any
    input_spec: Any
    def __init__(self, rate, data_format: Any | None = ..., **kwargs) -> None: ...

class SpatialDropout3D(Dropout):
    data_format: Any
    input_spec: Any
    def __init__(self, rate, data_format: Any | None = ..., **kwargs) -> None: ...

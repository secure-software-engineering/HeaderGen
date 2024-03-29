from typing import Any

from keras import backend as backend
from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class Pooling1D(Layer):
    pool_function: Any
    pool_size: Any
    strides: Any
    padding: Any
    data_format: Any
    input_spec: Any
    def __init__(
        self,
        pool_function,
        pool_size,
        strides,
        padding: str = ...,
        data_format: str = ...,
        name: Any | None = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling1D(Pooling1D):
    def __init__(
        self,
        pool_size: int = ...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: str = ...,
        **kwargs
    ) -> None: ...

class AveragePooling1D(Pooling1D):
    def __init__(
        self,
        pool_size: int = ...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: str = ...,
        **kwargs
    ) -> None: ...

class Pooling2D(Layer):
    pool_function: Any
    pool_size: Any
    strides: Any
    padding: Any
    data_format: Any
    input_spec: Any
    def __init__(
        self,
        pool_function,
        pool_size,
        strides,
        padding: str = ...,
        data_format: Any | None = ...,
        name: Any | None = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling2D(Pooling2D):
    def __init__(
        self,
        pool_size=...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        **kwargs
    ) -> None: ...

class AveragePooling2D(Pooling2D):
    def __init__(
        self,
        pool_size=...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        **kwargs
    ) -> None: ...

class Pooling3D(Layer):
    pool_function: Any
    pool_size: Any
    strides: Any
    padding: Any
    data_format: Any
    input_spec: Any
    def __init__(
        self,
        pool_function,
        pool_size,
        strides,
        padding: str = ...,
        data_format: str = ...,
        name: Any | None = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling3D(Pooling3D):
    def __init__(
        self,
        pool_size=...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        **kwargs
    ) -> None: ...

class AveragePooling3D(Pooling3D):
    def __init__(
        self,
        pool_size=...,
        strides: Any | None = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        **kwargs
    ) -> None: ...

class GlobalPooling1D(Layer):
    input_spec: Any
    data_format: Any
    keepdims: Any
    def __init__(
        self, data_format: str = ..., keepdims: bool = ..., **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling1D(GlobalPooling1D):
    supports_masking: bool
    def __init__(self, data_format: str = ..., **kwargs) -> None: ...
    def call(self, inputs, mask: Any | None = ...): ...
    def compute_mask(self, inputs, mask: Any | None = ...) -> None: ...

class GlobalMaxPooling1D(GlobalPooling1D):
    def call(self, inputs): ...

class GlobalPooling2D(Layer):
    data_format: Any
    input_spec: Any
    keepdims: Any
    def __init__(
        self, data_format: Any | None = ..., keepdims: bool = ..., **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling2D(GlobalPooling2D):
    def call(self, inputs): ...

class GlobalMaxPooling2D(GlobalPooling2D):
    def call(self, inputs): ...

class GlobalPooling3D(Layer):
    data_format: Any
    input_spec: Any
    keepdims: Any
    def __init__(
        self, data_format: Any | None = ..., keepdims: bool = ..., **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling3D(GlobalPooling3D):
    def call(self, inputs): ...

class GlobalMaxPooling3D(GlobalPooling3D):
    def call(self, inputs): ...

AvgPool1D = AveragePooling1D
MaxPool1D = MaxPooling1D
AvgPool2D = AveragePooling2D
MaxPool2D = MaxPooling2D
AvgPool3D = AveragePooling3D
MaxPool3D = MaxPooling3D
GlobalMaxPool1D = GlobalMaxPooling1D
GlobalMaxPool2D = GlobalMaxPooling2D
GlobalMaxPool3D = GlobalMaxPooling3D
GlobalAvgPool1D = GlobalAveragePooling1D
GlobalAvgPool2D = GlobalAveragePooling2D
GlobalAvgPool3D = GlobalAveragePooling3D

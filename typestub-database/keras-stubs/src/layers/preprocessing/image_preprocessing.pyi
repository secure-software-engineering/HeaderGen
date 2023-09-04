from typing import Any

from keras import backend as backend
from keras.preprocessing.image import smart_resize as smart_resize
from keras.src.engine import base_layer as base_layer
from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.utils import control_flow_util as control_flow_util

ResizeMethod: Any
H_AXIS: int
W_AXIS: int

def check_fill_mode_and_interpolation(fill_mode, interpolation) -> None: ...

class Resizing(base_layer.Layer):
    height: Any
    width: Any
    interpolation: Any
    crop_to_aspect_ratio: Any
    def __init__(
        self,
        height,
        width,
        interpolation: str = ...,
        crop_to_aspect_ratio: bool = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class CenterCrop(base_layer.Layer):
    height: Any
    width: Any
    def __init__(self, height, width, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomCrop(base_layer.BaseRandomLayer):
    height: Any
    width: Any
    seed: Any
    def __init__(self, height, width, seed: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Rescaling(base_layer.Layer):
    scale: Any
    offset: Any
    def __init__(self, scale, offset: float = ..., **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

HORIZONTAL: str
VERTICAL: str
HORIZONTAL_AND_VERTICAL: str

class RandomFlip(base_layer.BaseRandomLayer):
    mode: Any
    horizontal: bool
    vertical: bool
    seed: Any
    def __init__(self, mode=..., seed: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomTranslation(base_layer.BaseRandomLayer):
    height_factor: Any
    height_lower: Any
    height_upper: Any
    width_factor: Any
    width_lower: Any
    width_upper: Any
    fill_mode: Any
    fill_value: Any
    interpolation: Any
    seed: Any
    def __init__(
        self,
        height_factor,
        width_factor,
        fill_mode: str = ...,
        interpolation: str = ...,
        seed: Any | None = ...,
        fill_value: float = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def get_translation_matrix(translations, name: Any | None = ...): ...
def transform(
    images,
    transforms,
    fill_mode: str = ...,
    fill_value: float = ...,
    interpolation: str = ...,
    output_shape: Any | None = ...,
    name: Any | None = ...,
): ...
def get_rotation_matrix(angles, image_height, image_width, name: Any | None = ...): ...

class RandomRotation(base_layer.BaseRandomLayer):
    factor: Any
    lower: Any
    upper: Any
    fill_mode: Any
    fill_value: Any
    interpolation: Any
    seed: Any
    def __init__(
        self,
        factor,
        fill_mode: str = ...,
        interpolation: str = ...,
        seed: Any | None = ...,
        fill_value: float = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomZoom(base_layer.BaseRandomLayer):
    height_factor: Any
    height_lower: Any
    height_upper: Any
    width_factor: Any
    width_lower: Any
    width_upper: Any
    fill_mode: Any
    fill_value: Any
    interpolation: Any
    seed: Any
    def __init__(
        self,
        height_factor,
        width_factor: Any | None = ...,
        fill_mode: str = ...,
        interpolation: str = ...,
        seed: Any | None = ...,
        fill_value: float = ...,
        **kwargs
    ) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def get_zoom_matrix(zooms, image_height, image_width, name: Any | None = ...): ...

class RandomContrast(base_layer.BaseRandomLayer):
    factor: Any
    lower: Any
    upper: Any
    seed: Any
    def __init__(self, factor, seed: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomHeight(base_layer.BaseRandomLayer):
    factor: Any
    height_lower: Any
    height_upper: Any
    interpolation: Any
    seed: Any
    def __init__(
        self, factor, interpolation: str = ..., seed: Any | None = ..., **kwargs
    ) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class RandomWidth(base_layer.BaseRandomLayer):
    factor: Any
    width_lower: Any
    width_upper: Any
    interpolation: Any
    seed: Any
    def __init__(
        self, factor, interpolation: str = ..., seed: Any | None = ..., **kwargs
    ) -> None: ...
    def call(self, inputs, training: bool = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

def get_interpolation(interpolation): ...

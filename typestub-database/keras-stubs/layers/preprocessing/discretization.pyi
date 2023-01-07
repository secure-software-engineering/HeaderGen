from keras import backend as backend
from keras.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.utils import layer_utils as layer_utils, tf_utils as tf_utils
from typing import Any

INT: Any
MULTI_HOT: Any
ONE_HOT: Any
COUNT: Any

def summarize(values, epsilon): ...
def compress(summary, epsilon): ...
def merge_summaries(prev_summary, next_summary, epsilon): ...
def get_bin_boundaries(summary, num_bins): ...

class Discretization(base_preprocessing_layer.PreprocessingLayer):
    input_bin_boundaries: Any
    bin_boundaries: Any
    num_bins: Any
    epsilon: Any
    output_mode: Any
    sparse: Any
    def __init__(self, bin_boundaries: Any | None = ..., num_bins: Any | None = ..., epsilon: float = ..., output_mode: str = ..., sparse: bool = ..., **kwargs) -> None: ...
    summary: Any
    def build(self, input_shape): ...
    def adapt(self, data, batch_size: Any | None = ..., steps: Any | None = ...) -> None: ...
    def update_state(self, data) -> None: ...
    def finalize_state(self) -> None: ...
    def reset_state(self) -> None: ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def call(self, inputs): ...

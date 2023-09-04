from typing import Any

import numpy
from keras import backend as backend
from keras import optimizer_v1 as optimizer_v1
from keras import optimizers as optimizers
from keras.mixed_precision import policy as policy
from keras.src.engine import base_layer as base_layer
from keras.src.engine import base_layer_utils as base_layer_utils
from keras.src.engine import compile_utils as compile_utils
from keras.src.engine import data_adapter as data_adapter
from keras.src.engine import training_utils as training_utils
from keras.src.saving import hdf5_format as hdf5_format
from keras.src.saving import pickle_utils as pickle_utils
from keras.src.saving import save as save
from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import json_utils as json_utils
from keras.src.saving.saved_model import model_serialization as model_serialization
from keras.utils import generic_utils as generic_utils
from keras.utils import layer_utils as layer_utils
from keras.utils import object_identity as object_identity
from keras.utils import tf_utils as tf_utils
from keras.utils import traceback_utils as traceback_utils
from keras.utils import version_utils as version_utils
from keras.utils.io_utils import (
    ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite,
)
from keras.utils.io_utils import path_to_string as path_to_string
from keras.utils.mode_keys import ModeKeys as ModeKeys

class Model(base_layer.Layer, version_utils.ModelVersionSelector):
    def __new__(cls, *args, **kwargs): ...
    inputs: Any
    outputs: Any
    input_names: Any
    output_names: Any
    stop_training: bool
    history: Any
    compiled_loss: Any
    compiled_metrics: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __reduce__(self): ...
    def __deepcopy__(self, memo): ...
    def __copy__(self): ...
    def build(self, input_shape) -> None: ...
    def call(
        self, inputs, training: Any | None = ..., mask: Any | None = ...
    ) -> None: ...
    optimizer: Any
    loss: Any
    def compile(
        self,
        optimizer: str = ...,
        loss: Any | None = ...,
        metrics: Any | None = ...,
        loss_weights: Any | None = ...,
        weighted_metrics: Any | None = ...,
        run_eagerly: Any | None = ...,
        steps_per_execution: Any | None = ...,
        jit_compile: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def metrics(self): ...
    @property
    def metrics_names(self): ...
    @property
    def distribute_strategy(self): ...
    @property
    def run_eagerly(self): ...
    @run_eagerly.setter
    def run_eagerly(self, value) -> None: ...
    def train_step(self, data): ...
    def compute_loss(
        self,
        x: Any | None = ...,
        y: Any | None = ...,
        y_pred: Any | None = ...,
        sample_weight: Any | None = ...,
    ): ...
    def compute_metrics(self, x, y, y_pred, sample_weight): ...
    train_tf_function: Any
    train_function: Any
    def make_train_function(self, force: bool = ...): ...
    def fit(
        self,
        x: Any | None = ...,
        y: Any | None = ...,
        batch_size: Any | None = ...,
        epochs: int = ...,
        verbose: str = ...,
        callbacks: Any | None = ...,
        validation_split: float = ...,
        validation_data: Any | None = ...,
        shuffle: bool = ...,
        class_weight: Any | None = ...,
        sample_weight: Any | None = ...,
        initial_epoch: int = ...,
        steps_per_epoch: Any | None = ...,
        validation_steps: Any | None = ...,
        validation_batch_size: Any | None = ...,
        validation_freq: int = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
    ): ...
    def test_step(self, data): ...
    test_function: Any
    def make_test_function(self, force: bool = ...): ...
    def evaluate(
        self,
        x: Any | None = ...,
        y: Any | None = ...,
        batch_size: Any | None = ...,
        verbose: int = ...,
        sample_weight: Any | None = ...,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
        return_dict: bool = ...,
        **kwargs
    ): ...
    def predict_step(self, data): ...
    predict_function: Any
    def make_predict_function(self, force: bool = ...): ...
    def predict(
        self,
        x,
        batch_size: Any | None = ...,
        verbose: int = ...,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
    ) -> numpy.ndarray: ...
    # Deprecated
    def predict_proba(
        self,
        x,
        batch_size: Any | None = ...,
        verbose: int = ...,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
    ) -> numpy.ndarray: ...
    def reset_metrics(self) -> None: ...
    def train_on_batch(
        self,
        x,
        y: Any | None = ...,
        sample_weight: Any | None = ...,
        class_weight: Any | None = ...,
        reset_metrics: bool = ...,
        return_dict: bool = ...,
    ): ...
    def test_on_batch(
        self,
        x,
        y: Any | None = ...,
        sample_weight: Any | None = ...,
        reset_metrics: bool = ...,
        return_dict: bool = ...,
    ): ...
    def predict_on_batch(self, x): ...
    def fit_generator(
        self,
        generator,
        steps_per_epoch: Any | None = ...,
        epochs: int = ...,
        verbose: int = ...,
        callbacks: Any | None = ...,
        validation_data: Any | None = ...,
        validation_steps: Any | None = ...,
        validation_freq: int = ...,
        class_weight: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
        shuffle: bool = ...,
        initial_epoch: int = ...,
    ): ...
    def evaluate_generator(
        self,
        generator,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
        verbose: int = ...,
    ): ...
    def predict_generator(
        self,
        generator,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
        verbose: int = ...,
    ): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def get_weights(self): ...
    def save(
        self,
        filepath,
        overwrite: bool = ...,
        include_optimizer: bool = ...,
        save_format: Any | None = ...,
        signatures: Any | None = ...,
        options: Any | None = ...,
        save_traces: bool = ...,
    ) -> None: ...
    def save_weights(
        self,
        filepath,
        overwrite: bool = ...,
        save_format: Any | None = ...,
        options: Any | None = ...,
    ) -> None: ...
    def load_weights(
        self,
        filepath,
        by_name: bool = ...,
        skip_mismatch: bool = ...,
        options: Any | None = ...,
    ): ...
    def get_config(self) -> None: ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...
    def to_json(self, **kwargs): ...
    def to_yaml(self, **kwargs) -> None: ...
    def reset_states(self) -> None: ...
    @property
    def state_updates(self): ...
    @property
    def weights(self): ...
    def summary(
        self,
        line_length: Any | None = ...,
        positions: Any | None = ...,
        print_fn: Any | None = ...,
        expand_nested: bool = ...,
        show_trainable: bool = ...,
    ) -> None: ...
    @property
    def layers(self): ...
    @layers.setter
    def layers(self, _) -> None: ...
    def get_layer(self, name: Any | None = ..., index: Any | None = ...): ...
    def save_spec(self, dynamic_batch: bool = ...): ...

def reduce_per_replica(values, strategy, reduction: str = ...): ...
def concat(tensors, axis: int = ...): ...
def flatten_metrics_in_order(logs, metrics_names): ...
def saver_with_op_caching(obj): ...
def disable_multi_worker(method): ...
def inject_functional_model_class(cls): ...
def is_functional_model_init_params(args, kwargs): ...

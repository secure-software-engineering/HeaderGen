from typing import Any

from keras import backend as backend
from keras import losses as losses
from keras import optimizer_v1 as optimizer_v1
from keras import optimizers as optimizers
from keras.distribute import distributed_training_utils as distributed_training_utils
from keras.distribute import (
    distributed_training_utils_v1 as distributed_training_utils_v1,
)
from keras.mixed_precision import loss_scale_optimizer as loss_scale_optimizer
from keras.mixed_precision import policy as policy
from keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from keras.src.engine import base_layer as base_layer
from keras.src.engine import training as training_lib
from keras.src.engine import training_arrays_v1 as training_arrays_v1
from keras.src.engine import training_distributed_v1 as training_distributed_v1
from keras.src.engine import training_eager_v1 as training_eager_v1
from keras.src.engine import training_generator_v1 as training_generator_v1
from keras.src.engine import training_utils as training_utils
from keras.src.engine import training_utils_v1 as training_utils_v1
from keras.src.saving import saving_utils as saving_utils
from keras.src.saving.saved_model import model_serialization as model_serialization
from keras.utils import data_utils as data_utils
from keras.utils import layer_utils as layer_utils
from keras.utils import losses_utils as losses_utils
from keras.utils import tf_inspect as tf_inspect
from keras.utils import tf_utils as tf_utils
from keras.utils.mode_keys import ModeKeys as ModeKeys

class Model(training_lib.Model):
    def __init__(self, *args, **kwargs) -> None: ...
    def get_weights(self): ...
    def load_weights(
        self, filepath, by_name: bool = ..., skip_mismatch: bool = ...
    ): ...
    loss: Any
    loss_weights: Any
    sample_weight_mode: Any
    loss_functions: Any
    train_function: Any
    test_function: Any
    predict_function: Any
    def compile(
        self,
        optimizer: str = ...,
        loss: Any | None = ...,
        metrics: Any | None = ...,
        loss_weights: Any | None = ...,
        sample_weight_mode: Any | None = ...,
        weighted_metrics: Any | None = ...,
        target_tensors: Any | None = ...,
        distribute: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def metrics(self): ...
    @property
    def metrics_names(self): ...
    @property
    def run_eagerly(self): ...
    @run_eagerly.setter
    def run_eagerly(self, value) -> None: ...
    def fit(
        self,
        x: Any | None = ...,
        y: Any | None = ...,
        batch_size: Any | None = ...,
        epochs: int = ...,
        verbose: int = ...,
        callbacks: Any | None = ...,
        validation_split: float = ...,
        validation_data: Any | None = ...,
        shuffle: bool = ...,
        class_weight: Any | None = ...,
        sample_weight: Any | None = ...,
        initial_epoch: int = ...,
        steps_per_epoch: Any | None = ...,
        validation_steps: Any | None = ...,
        validation_freq: int = ...,
        max_queue_size: int = ...,
        workers: int = ...,
        use_multiprocessing: bool = ...,
        **kwargs
    ): ...
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
    ): ...
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
    ): ...
    def reset_metrics(self) -> None: ...
    def train_on_batch(
        self,
        x,
        y: Any | None = ...,
        sample_weight: Any | None = ...,
        class_weight: Any | None = ...,
        reset_metrics: bool = ...,
    ): ...
    def test_on_batch(
        self,
        x,
        y: Any | None = ...,
        sample_weight: Any | None = ...,
        reset_metrics: bool = ...,
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
    def sample_weights(self): ...

class DistributedCallbackModel(Model):
    optimizer: Any
    def __init__(self, model) -> None: ...
    def set_original_model(self, orig_model) -> None: ...
    def save_weights(
        self, filepath, overwrite: bool = ..., save_format: Any | None = ...
    ) -> None: ...
    def save(
        self, filepath, overwrite: bool = ..., include_optimizer: bool = ...
    ) -> None: ...
    def load_weights(self, filepath, by_name: bool = ...) -> None: ...
    def __getattr__(self, item): ...

class _TrainingEndpoint:
    def __init__(
        self,
        output,
        output_name,
        loss_fn,
        loss_weight: Any | None = ...,
        training_target: Any | None = ...,
        output_loss_metric: Any | None = ...,
        sample_weight: Any | None = ...,
        sample_weight_mode: Any | None = ...,
    ) -> None: ...
    @property
    def output(self): ...
    @property
    def output_name(self): ...
    @property
    def shape(self): ...
    @property
    def loss_fn(self): ...
    @property
    def loss_weight(self): ...
    @loss_weight.setter
    def loss_weight(self, value) -> None: ...
    @property
    def training_target(self): ...
    @training_target.setter
    def training_target(self, value) -> None: ...
    def create_training_target(self, target, run_eagerly: bool = ...) -> None: ...
    @property
    def output_loss_metric(self): ...
    @output_loss_metric.setter
    def output_loss_metric(self, value) -> None: ...
    @property
    def sample_weight(self): ...
    @sample_weight.setter
    def sample_weight(self, value) -> None: ...
    @property
    def sample_weight_mode(self): ...
    @sample_weight_mode.setter
    def sample_weight_mode(self, value) -> None: ...
    def should_skip_target(self): ...
    def should_skip_target_weights(self): ...
    def has_training_target(self): ...
    def has_feedable_training_target(self): ...
    def loss_name(self): ...
    @property
    def feed_output_shape(self): ...
    def sample_weights_mismatch(self): ...
    def populate_sample_weight(self, sample_weight, sample_weight_mode) -> None: ...

class _TrainingTarget:
    def __init__(
        self, target, feedable: bool = ..., skip_target_weights: bool = ...
    ) -> None: ...
    @property
    def target(self): ...
    @property
    def feedable(self): ...
    @property
    def skip_target_weights(self): ...

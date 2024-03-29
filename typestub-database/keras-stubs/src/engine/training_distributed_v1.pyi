from typing import Any

from keras import backend as backend
from keras.src.engine import training_arrays_v1 as training_arrays_v1
from keras.src.engine import training_utils_v1 as training_utils_v1
from keras.utils.generic_utils import Progbar as Progbar
from keras.utils.mode_keys import ModeKeys as ModeKeys

def experimental_tpu_fit_loop(
    model,
    dataset,
    epochs: int = ...,
    verbose: int = ...,
    callbacks: Any | None = ...,
    initial_epoch: int = ...,
    steps_per_epoch: Any | None = ...,
    val_dataset: Any | None = ...,
    validation_steps: Any | None = ...,
    validation_freq: int = ...,
): ...
def experimental_tpu_test_loop(
    model,
    dataset,
    verbose: int = ...,
    steps: Any | None = ...,
    callbacks: Any | None = ...,
): ...
def experimental_tpu_predict_loop(
    model,
    dataset,
    verbose: int = ...,
    steps: Any | None = ...,
    callbacks: Any | None = ...,
): ...

class DistributionSingleWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    def fit(
        self,
        model,
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
        **kwargs
    ): ...
    def evaluate(
        self,
        model,
        x: Any | None = ...,
        y: Any | None = ...,
        batch_size: Any | None = ...,
        verbose: int = ...,
        sample_weight: Any | None = ...,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        **kwargs
    ): ...
    def predict(
        self,
        model,
        x,
        batch_size: Any | None = ...,
        verbose: int = ...,
        steps: Any | None = ...,
        callbacks: Any | None = ...,
        **kwargs
    ): ...

class DistributionMultiWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    def __init__(self, single_worker_loop) -> None: ...
    def fit(self, *args, **kwargs): ...
    def evaluate(self, *args, **kwargs): ...
    def predict(self, *args, **kwargs): ...

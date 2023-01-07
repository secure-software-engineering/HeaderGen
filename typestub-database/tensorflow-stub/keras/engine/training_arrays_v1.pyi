from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.distribute import distributed_training_utils_v1 as distributed_training_utils_v1
from tensorflow.python.keras.engine import training_utils_v1 as training_utils_v1
from tensorflow.python.keras.utils.generic_utils import make_batches as make_batches, slice_arrays as slice_arrays
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.util import nest as nest
from typing import Any

def model_iteration(model, inputs, targets: Any | None = ..., sample_weights: Any | None = ..., batch_size: Any | None = ..., epochs: int = ..., verbose: int = ..., callbacks: Any | None = ..., val_inputs: Any | None = ..., val_targets: Any | None = ..., val_sample_weights: Any | None = ..., shuffle: bool = ..., initial_epoch: int = ..., steps_per_epoch: Any | None = ..., validation_steps: Any | None = ..., validation_freq: int = ..., mode=..., validation_in_fit: bool = ..., prepared_feed_values_from_dataset: bool = ..., steps_name: str = ..., **kwargs): ...

fit_loop: Any
test_loop: Any
predict_loop: Any

class ArrayLikeTrainingLoop(training_utils_v1.TrainingLoop):
    def fit(self, model, x: Any | None = ..., y: Any | None = ..., batch_size: Any | None = ..., epochs: int = ..., verbose: int = ..., callbacks: Any | None = ..., validation_split: float = ..., validation_data: Any | None = ..., shuffle: bool = ..., class_weight: Any | None = ..., sample_weight: Any | None = ..., initial_epoch: int = ..., steps_per_epoch: Any | None = ..., validation_steps: Any | None = ..., validation_freq: int = ..., **kwargs): ...
    def evaluate(self, model, x: Any | None = ..., y: Any | None = ..., batch_size: Any | None = ..., verbose: int = ..., sample_weight: Any | None = ..., steps: Any | None = ..., callbacks: Any | None = ..., **kwargs): ...
    def predict(self, model, x, batch_size: Any | None = ..., verbose: int = ..., steps: Any | None = ..., callbacks: Any | None = ..., **kwargs): ...

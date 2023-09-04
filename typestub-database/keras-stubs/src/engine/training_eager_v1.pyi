from typing import Any

from keras import backend as backend
from keras.mixed_precision import loss_scale_optimizer as loss_scale_optimizer
from keras.src.engine import training_utils as training_utils
from keras.src.engine import training_utils_v1 as training_utils_v1
from keras.utils import losses_utils as losses_utils

def train_on_batch(
    model,
    inputs,
    targets,
    sample_weights: Any | None = ...,
    output_loss_metrics: Any | None = ...,
): ...
def test_on_batch(
    model,
    inputs,
    targets,
    sample_weights: Any | None = ...,
    output_loss_metrics: Any | None = ...,
): ...

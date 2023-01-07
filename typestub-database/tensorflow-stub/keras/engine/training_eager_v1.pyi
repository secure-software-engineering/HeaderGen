from tensorflow.python.eager.backprop import GradientTape as GradientTape
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import training_utils as training_utils, training_utils_v1 as training_utils_v1
from tensorflow.python.keras.mixed_precision import loss_scale_optimizer as loss_scale_optimizer
from tensorflow.python.keras.utils import losses_utils as losses_utils
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util import nest as nest
from typing import Any

def train_on_batch(model, inputs, targets, sample_weights: Any | None = ..., output_loss_metrics: Any | None = ...): ...
def test_on_batch(model, inputs, targets, sample_weights: Any | None = ..., output_loss_metrics: Any | None = ...): ...

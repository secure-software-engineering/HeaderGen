from enum import Enum
from tensorflow.python.compat import compat as compat
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.utils import losses_utils as losses_utils, tf_utils as tf_utils
from tensorflow.python.keras.utils.generic_utils import to_list as to_list
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, clip_ops as clip_ops, control_flow_ops as control_flow_ops, gen_math_ops as gen_math_ops, math_ops as math_ops, nn_ops as nn_ops, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import tf_decorator as tf_decorator
from typing import Any

NEG_INF: Any

class Reduction(Enum):
    SUM: str
    SUM_OVER_BATCH_SIZE: str
    WEIGHTED_MEAN: str

def update_state_wrapper(update_state_fn): ...
def result_wrapper(result_fn): ...
def weakmethod(method): ...
def assert_thresholds_range(thresholds) -> None: ...
def parse_init_thresholds(thresholds, default_threshold: float = ...): ...

class ConfusionMatrix(Enum):
    TRUE_POSITIVES: str
    FALSE_POSITIVES: str
    TRUE_NEGATIVES: str
    FALSE_NEGATIVES: str

class AUCCurve(Enum):
    ROC: str
    PR: str
    @staticmethod
    def from_str(key): ...

class AUCSummationMethod(Enum):
    INTERPOLATION: str
    MAJORING: str
    MINORING: str
    @staticmethod
    def from_str(key): ...

def is_evenly_distributed_thresholds(thresholds): ...
def update_confusion_matrix_variables(variables_to_update, y_true, y_pred, thresholds, top_k: Any | None = ..., class_id: Any | None = ..., sample_weight: Any | None = ..., multi_label: bool = ..., label_weights: Any | None = ..., thresholds_distributed_evenly: bool = ...): ...
def ragged_assert_compatible_and_get_flat_values(values, mask: Any | None = ...): ...

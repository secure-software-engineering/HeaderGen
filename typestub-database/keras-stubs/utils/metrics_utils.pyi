from enum import Enum
from keras import backend as backend
from keras.utils import losses_utils as losses_utils, tf_utils as tf_utils
from keras.utils.generic_utils import to_list as to_list
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

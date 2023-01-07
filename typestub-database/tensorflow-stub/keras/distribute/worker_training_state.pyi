from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.distribute import distributed_file_utils as distributed_file_utils
from tensorflow.python.keras.utils import mode_keys as mode_keys
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.training import checkpoint_management as checkpoint_management
from typing import Any

CKPT_SAVED_EPOCH: str
CKPT_SAVED_EPOCH_UNUSED_VALUE: int

class WorkerTrainingState:
    read_checkpoint_manager: Any
    write_checkpoint_manager: Any
    def __init__(self, model, checkpoint_dir) -> None: ...
    def back_up(self, epoch) -> None: ...
    def restore(self) -> None: ...
    def delete_backup(self) -> None: ...
    def maybe_load_initial_epoch_from_ckpt(self, initial_epoch, mode): ...

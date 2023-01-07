from keras import backend as backend
from keras.distribute import distributed_file_utils as distributed_file_utils
from keras.utils import mode_keys as mode_keys
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

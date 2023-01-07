from tensorflow.python.framework import constant_op as constant_op
from tensorflow.python.training.tracking import base as base

class SaveableHook(base.NoRestoreSaveable):
    def __init__(self, name) -> None: ...
    @property
    def device(self): ...
    def before_save(self) -> None: ...
    def after_restore(self) -> None: ...

import collections

class KerasModeKeys:
    TRAIN: str
    TEST: str
    PREDICT: str

class EstimatorModeKeys:
    TRAIN: str
    EVAL: str
    PREDICT: str

def is_predict(mode): ...
def is_eval(mode): ...
def is_train(mode): ...

class ModeKeyMap(collections.abc.Mapping):
    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self): ...

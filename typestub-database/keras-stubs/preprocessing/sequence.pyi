import abc
from keras.utils import data_utils as data_utils
from keras_preprocessing import sequence
from typing import Any

make_sampling_table: Any
skipgrams: Any

class TimeseriesGenerator(sequence.TimeseriesGenerator, data_utils.Sequence, metaclass=abc.ABCMeta): ...

def pad_sequences(sequences, maxlen: Any | None = ..., dtype: str = ..., padding: str = ..., truncating: str = ..., value: float = ...): ...

import abc
from tensorflow.python.training.tracking import base as base
from tensorflow.python.util.tf_export import tf_export as tf_export

class PythonState(base.Trackable, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def serialize(self): ...
    @abc.abstractmethod
    def deserialize(self, string_value): ...

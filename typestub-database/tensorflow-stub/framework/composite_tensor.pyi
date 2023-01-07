import abc
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class CompositeTensor(metaclass=abc.ABCMeta): ...

def replace_composites_with_components(structure): ...

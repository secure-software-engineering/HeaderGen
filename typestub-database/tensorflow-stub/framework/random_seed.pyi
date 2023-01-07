from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, ops as ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

DEFAULT_GRAPH_SEED: int

def get_seed(op_seed): ...
def set_random_seed(seed) -> None: ...
def set_seed(seed) -> None: ...

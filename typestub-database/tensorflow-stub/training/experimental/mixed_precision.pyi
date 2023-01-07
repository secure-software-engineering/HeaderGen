from tensorflow.python.framework import config as config
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training import optimizer as optimizer
from tensorflow.python.training.experimental import mixed_precision_global_state as mixed_precision_global_state
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def register_loss_scale_wrapper(optimizer_cls, wrapper_cls) -> None: ...
def enable_mixed_precision_graph_rewrite_v1(opt, loss_scale: str = ...): ...
def disable_mixed_precision_graph_rewrite_v1() -> None: ...

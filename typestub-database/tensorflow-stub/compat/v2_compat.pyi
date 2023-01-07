from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import counter as counter, interleave_ops as interleave_ops, random_ops as random_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, readers as readers
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import control_flow_v2_toggles as control_flow_v2_toggles, variable_scope as variable_scope
from tensorflow.python.util.tf_export import tf_export as tf_export

def enable_v2_behavior() -> None: ...
def disable_v2_behavior() -> None: ...

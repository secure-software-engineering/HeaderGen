from tensorflow.python.ops.gen_batch_ops import *
from tensorflow.python.eager import function as function
from tensorflow.python.framework import ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_batch_ops as gen_batch_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def batch_function(num_batch_threads, max_batch_size, batch_timeout_micros, allowed_batch_sizes: Any | None = ..., max_enqueued_batches: int = ..., autograph: bool = ..., enable_large_batch_splitting: bool = ...): ...

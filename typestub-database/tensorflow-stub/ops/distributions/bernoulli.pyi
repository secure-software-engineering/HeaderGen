from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution, kullback_leibler as kullback_leibler
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class Bernoulli(distribution.Distribution):
    def __init__(self, logits: Any | None = ..., probs: Any | None = ..., dtype=..., validate_args: bool = ..., allow_nan_stats: bool = ..., name: str = ...) -> None: ...
    @property
    def logits(self): ...
    @property
    def probs(self): ...

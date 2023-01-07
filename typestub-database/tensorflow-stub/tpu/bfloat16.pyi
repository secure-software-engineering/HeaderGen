from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops import math_ops as math_ops, variable_scope as variable_scope
from tensorflow.python.util import tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Generator, Optional, Text

def bfloat16_scope(name: Optional[Text] = ...) -> Generator[variable_scope.variable_scope, None, None]: ...

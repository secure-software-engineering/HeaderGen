from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, gen_ragged_math_ops as gen_ragged_math_ops, math_ops as math_ops
from typing import Any

def assert_splits_match(nested_splits_lists): ...

get_positive_axis: Any
convert_to_int_tensor: Any
repeat: Any

def lengths_to_splits(lengths): ...
def repeat_ranges(params, splits, repeats): ...

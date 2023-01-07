from tensorflow.python.framework import errors_impl as errors_impl
from tensorflow.python.platform import flags as flags
from tensorflow.python.training import py_checkpoint_reader as py_checkpoint_reader
from typing import Any

FLAGS: Any

def print_tensors_in_checkpoint_file(file_name, tensor_name, all_tensors, all_tensor_names: bool = ..., count_exclude_pattern: str = ...) -> None: ...
def parse_numpy_printoption(kv_str) -> None: ...
def main(unused_argv) -> None: ...

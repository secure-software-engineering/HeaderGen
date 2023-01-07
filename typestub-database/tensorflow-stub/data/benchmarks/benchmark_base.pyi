from tensorflow.python.client import session as session
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.eager import context as context
from tensorflow.python.platform import test as test
from typing import Any

class DatasetBenchmarkBase(test.Benchmark):
    def run_op_benchmark(self, op, iters: int = ..., warmup: bool = ..., session_config: Any | None = ...): ...
    def run_benchmark(self, dataset, num_elements, iters: int = ..., warmup: bool = ..., apply_default_optimizations: bool = ..., session_config: Any | None = ...): ...
    def run_and_report_benchmark(self, dataset, num_elements, name, iters: int = ..., extras: Any | None = ..., warmup: bool = ..., apply_default_optimizations: bool = ..., session_config: Any | None = ...): ...

from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.core.util import test_log_pb2 as test_log_pb2
from tensorflow.python.client import timeline as timeline
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

GLOBAL_BENCHMARK_REGISTRY: Any
TEST_REPORTER_TEST_ENV: str
OVERRIDE_GLOBAL_THREADPOOL: str

class _BenchmarkRegistrar(type):
    def __new__(mcs, clsname, base, attrs): ...

class ParameterizedBenchmark(_BenchmarkRegistrar):
    def __new__(mcs, clsname, base, attrs): ...

class Benchmark:
    @classmethod
    def is_abstract(cls): ...
    def report_benchmark(self, iters: Any | None = ..., cpu_time: Any | None = ..., wall_time: Any | None = ..., throughput: Any | None = ..., extras: Any | None = ..., name: Any | None = ..., metrics: Any | None = ...) -> None: ...

def benchmark_config(): ...

class TensorFlowBenchmark(Benchmark):
    def __init__(self) -> None: ...
    @classmethod
    def is_abstract(cls): ...
    def run_op_benchmark(self, sess, op_or_tensor, feed_dict: Any | None = ..., burn_iters: int = ..., min_iters: int = ..., store_trace: bool = ..., store_memory_usage: bool = ..., name: Any | None = ..., extras: Any | None = ..., mbs: int = ...): ...
    def evaluate(self, tensors): ...

def benchmarks_main(true_main, argv: Any | None = ...): ...

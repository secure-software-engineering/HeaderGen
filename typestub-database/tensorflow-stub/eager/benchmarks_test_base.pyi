from tensorflow.python.eager import test as test
from tensorflow.python.platform import flags as flags
from typing import Any

class MicroBenchmarksBase(test.Benchmark):
    def run_with_xprof(self, enable_python_trace, run_benchmark, func, num_iters_xprof, execution_mode, suid): ...
    def run_report(self, run_benchmark, func, num_iters, execution_mode: Any | None = ...) -> None: ...

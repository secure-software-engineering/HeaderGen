import enum
from tensorflow.core.framework import dataset_options_pb2 as dataset_options_pb2
from tensorflow.python.data.util import options as options_lib
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class AutoShardPolicy(enum.IntEnum):
    OFF: int
    AUTO: int
    FILE: int
    DATA: int
    HINT: int

class ExternalStatePolicy(enum.Enum):
    WARN: int
    IGNORE: int
    FAIL: int

class AutotuneOptions(options_lib.OptionsBase):
    enabled: Any
    cpu_budget: Any
    ram_budget: Any

class DistributeOptions(options_lib.OptionsBase):
    auto_shard_policy: Any
    num_devices: Any

class OptimizationOptions(options_lib.OptionsBase):
    apply_default_optimizations: Any
    filter_fusion: Any
    map_and_batch_fusion: Any
    map_and_filter_fusion: Any
    map_fusion: Any
    map_parallelization: Any
    noop_elimination: Any
    parallel_batch: Any
    shuffle_and_repeat_fusion: Any

class ThreadingOptions(options_lib.OptionsBase):
    max_intra_op_parallelism: Any
    private_threadpool_size: Any

class Options(options_lib.OptionsBase):
    autotune: Any
    deterministic: Any
    experimental_deterministic: Any
    experimental_distribute: Any
    experimental_external_state_policy: Any
    experimental_optimization: Any
    experimental_slack: Any
    experimental_threading: Any
    threading: Any
    def __getattribute__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def merge(self, options): ...

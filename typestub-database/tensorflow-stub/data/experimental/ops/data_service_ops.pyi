import enum
from tensorflow.core.protobuf import data_service_pb2 as data_service_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import compat as compat
from tensorflow.python.data.experimental.ops import compression_ops as compression_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.ops.options import AutoShardPolicy as AutoShardPolicy, ExternalStatePolicy as ExternalStatePolicy
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, string_ops as string_ops
from tensorflow.python.util import lazy_loader as lazy_loader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

COMPRESSION_AUTO: str
COMPRESSION_NONE: Any
nested_structure_coder: Any

class ShardingPolicy(enum.IntEnum):
    OFF: int
    DYNAMIC: int
    FILE: int
    DATA: int
    FILE_OR_DATA: int
    HINT: int

class _DataServiceDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, dataset_id, processing_mode, address, element_spec, protocol, data_transfer_protocol, job_name: Any | None = ..., consumer_index: Any | None = ..., num_consumers: Any | None = ..., max_outstanding_requests: Any | None = ..., task_refresh_interval_hint_ms: Any | None = ..., target_workers: str = ...) -> None: ...
    @property
    def element_spec(self): ...

class _DataServiceDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, dataset_id, processing_mode, address, element_spec, protocol, data_transfer_protocol, job_name, consumer_index, num_consumers, max_outstanding_requests, task_refresh_interval_hint_ms, target_workers) -> None: ...

def distribute(processing_mode, service, job_name: Any | None = ..., consumer_index: Any | None = ..., num_consumers: Any | None = ..., max_outstanding_requests: Any | None = ..., data_transfer_protocol: Any | None = ..., compression: str = ..., target_workers: str = ...): ...
def register_dataset(service, dataset, compression: str = ...): ...
def from_dataset_id(processing_mode, service, dataset_id, element_spec: Any | None = ..., job_name: Any | None = ..., consumer_index: Any | None = ..., num_consumers: Any | None = ..., max_outstanding_requests: Any | None = ..., data_transfer_protocol: Any | None = ..., target_workers: str = ...): ...

from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, random_seed as random_seed
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

COMPRESSION_GZIP: str
COMPRESSION_SNAPPY: str
COMPRESSION_NONE: Any

class _LegacySnapshotDataset(dataset_ops.UnaryUnchangedStructureDataset):
    def __init__(self, input_dataset, path, compression: Any | None = ..., reader_path_prefix: Any | None = ..., writer_path_prefix: Any | None = ..., shard_size_bytes: Any | None = ..., pending_snapshot_expiry_seconds: Any | None = ..., num_reader_threads: Any | None = ..., reader_buffer_size: Any | None = ..., num_writer_threads: Any | None = ..., writer_buffer_size: Any | None = ..., shuffle_on_read: Any | None = ..., shuffle_seed: Any | None = ..., mode: Any | None = ..., snapshot_name: Any | None = ...) -> None: ...

def legacy_snapshot(path, compression: Any | None = ..., reader_path_prefix: Any | None = ..., writer_path_prefix: Any | None = ..., shard_size_bytes: Any | None = ..., pending_snapshot_expiry_seconds: Any | None = ..., num_reader_threads: Any | None = ..., reader_buffer_size: Any | None = ..., num_writer_threads: Any | None = ..., writer_buffer_size: Any | None = ..., shuffle_on_read: Any | None = ..., shuffle_seed: Any | None = ..., mode: Any | None = ..., snapshot_name: Any | None = ...): ...
def snapshot(path, compression: str = ..., reader_func: Any | None = ..., shard_func: Any | None = ...): ...

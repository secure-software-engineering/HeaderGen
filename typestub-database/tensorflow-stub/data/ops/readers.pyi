from tensorflow.core.framework import dataset_metadata_pb2 as dataset_metadata_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import compat as compat
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, gen_dataset_ops as gen_dataset_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class _TextLineDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class TextLineDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class TextLineDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...) -> None: ...

class _TFRecordDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class ParallelInterleaveDataset(dataset_ops.UnaryDataset):
    def __init__(self, input_dataset, map_func, cycle_length, block_length, sloppy, buffer_output_elements, prefetch_input_elements, name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class TFRecordDatasetV2(dataset_ops.DatasetV2):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class TFRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames, compression_type: Any | None = ..., buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...) -> None: ...

class _FixedLengthRecordDataset(dataset_ops.DatasetSource):
    def __init__(self, filenames, record_bytes, header_bytes: Any | None = ..., footer_bytes: Any | None = ..., buffer_size: Any | None = ..., compression_type: Any | None = ..., name: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames, record_bytes, header_bytes: Any | None = ..., footer_bytes: Any | None = ..., buffer_size: Any | None = ..., compression_type: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...): ...
    @property
    def element_spec(self): ...

class FixedLengthRecordDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames, record_bytes, header_bytes: Any | None = ..., footer_bytes: Any | None = ..., buffer_size: Any | None = ..., compression_type: Any | None = ..., num_parallel_reads: Any | None = ..., name: Any | None = ...) -> None: ...
FixedLengthRecordDataset = FixedLengthRecordDatasetV2
TFRecordDataset = TFRecordDatasetV2
TextLineDataset = TextLineDatasetV2
FixedLengthRecordDataset = FixedLengthRecordDatasetV1
TFRecordDataset = TFRecordDatasetV1
TextLineDataset = TextLineDatasetV1

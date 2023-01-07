from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import error_ops as error_ops, parsing_ops as parsing_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert, nest as nest
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops, io_ops as io_ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def make_tf_record_dataset(file_pattern, batch_size, parser_fn: Any | None = ..., num_epochs: Any | None = ..., shuffle: bool = ..., shuffle_buffer_size: Any | None = ..., shuffle_seed: Any | None = ..., prefetch_buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., num_parallel_parser_calls: Any | None = ..., drop_final_batch: bool = ...): ...
def make_csv_dataset_v2(file_pattern, batch_size, column_names: Any | None = ..., column_defaults: Any | None = ..., label_name: Any | None = ..., select_columns: Any | None = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Any | None = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Any | None = ..., prefetch_buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Any | None = ..., ignore_errors: bool = ...): ...
def make_csv_dataset_v1(file_pattern, batch_size, column_names: Any | None = ..., column_defaults: Any | None = ..., label_name: Any | None = ..., select_columns: Any | None = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., header: bool = ..., num_epochs: Any | None = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Any | None = ..., prefetch_buffer_size: Any | None = ..., num_parallel_reads: Any | None = ..., sloppy: bool = ..., num_rows_for_inference: int = ..., compression_type: Any | None = ..., ignore_errors: bool = ...): ...

class CsvDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, filenames, record_defaults, compression_type: Any | None = ..., buffer_size: Any | None = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Any | None = ..., exclude_cols: Any | None = ...) -> None: ...
    @property
    def element_spec(self): ...

class CsvDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, filenames, record_defaults, compression_type: Any | None = ..., buffer_size: Any | None = ..., header: bool = ..., field_delim: str = ..., use_quote_delim: bool = ..., na_value: str = ..., select_cols: Any | None = ...) -> None: ...

def make_batched_features_dataset_v2(file_pattern, batch_size, features, reader: Any | None = ..., label_key: Any | None = ..., reader_args: Any | None = ..., num_epochs: Any | None = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Any | None = ..., prefetch_buffer_size: Any | None = ..., reader_num_threads: Any | None = ..., parser_num_threads: Any | None = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...
def make_batched_features_dataset_v1(file_pattern, batch_size, features, reader: Any | None = ..., label_key: Any | None = ..., reader_args: Any | None = ..., num_epochs: Any | None = ..., shuffle: bool = ..., shuffle_buffer_size: int = ..., shuffle_seed: Any | None = ..., prefetch_buffer_size: Any | None = ..., reader_num_threads: Any | None = ..., parser_num_threads: Any | None = ..., sloppy_ordering: bool = ..., drop_final_batch: bool = ...): ...

class SqlDatasetV2(dataset_ops.DatasetSource):
    def __init__(self, driver_name, data_source_name, query, output_types): ...
    @property
    def element_spec(self): ...

class SqlDatasetV1(dataset_ops.DatasetV1Adapter):
    def __init__(self, driver_name, data_source_name, query, output_types) -> None: ...
CsvDataset = CsvDatasetV2
SqlDataset = SqlDatasetV2
make_batched_features_dataset = make_batched_features_dataset_v2
make_csv_dataset = make_csv_dataset_v2
CsvDataset = CsvDatasetV1
SqlDataset = SqlDatasetV1
make_batched_features_dataset = make_batched_features_dataset_v1
make_csv_dataset = make_csv_dataset_v1

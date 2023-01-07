from tensorflow.python.data.experimental.ops import interleave_ops as interleave_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops, readers as readers
from tensorflow.python.framework import dtypes as dtypes, function as function, ops as ops
from tensorflow.python.ops import functional_ops as functional_ops
from typing import Callable, Optional, Text, Union

def StreamingFilesDataset(files: Union[Text, dataset_ops.Dataset], filetype: Optional[Union[Text, Callable[[Text], dataset_ops.Dataset]]] = ..., file_reader_job: Optional[Text] = ..., worker_job: Optional[Text] = ..., num_epochs: Optional[int] = ..., filename_shuffle_buffer_size: Optional[Union[int, bool]] = ..., num_parallel_reads: Optional[int] = ..., batch_transfer_size: Optional[Union[int, bool]] = ..., sloppy: bool = ...) -> dataset_ops.Dataset: ...

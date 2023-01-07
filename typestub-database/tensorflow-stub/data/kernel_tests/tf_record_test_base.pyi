from tensorflow.core.example import example_pb2 as example_pb2, feature_pb2 as feature_pb2
from tensorflow.python.data.experimental.ops import readers as readers
from tensorflow.python.data.kernel_tests import test_base as test_base
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.lib.io import python_io as python_io
from tensorflow.python.ops import parsing_ops as parsing_ops
from tensorflow.python.util import compat as compat
from typing import Any

class FeaturesTestBase(test_base.DatasetTestBase):
    def setUp(self) -> None: ...
    filenames: Any
    num_epochs: Any
    batch_size: Any
    def make_batch_feature(self, filenames, num_epochs, batch_size, label_key: Any | None = ..., reader_num_threads: int = ..., parser_num_threads: int = ..., shuffle: bool = ..., shuffle_seed: Any | None = ..., drop_final_batch: bool = ...): ...

class TFRecordTestBase(test_base.DatasetTestBase):
    def setUp(self) -> None: ...

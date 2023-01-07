from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context, wrap_function as wrap_function
from tensorflow.python.framework import convert_to_constants as convert_to_constants, dtypes as dtypes, errors as errors, graph_util as graph_util, importer as importer, ops as ops
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.ops import array_ops as array_ops, gen_resource_variable_ops as gen_resource_variable_ops
from tensorflow.python.saved_model import builder as builder, load as load, loader as loader, save as save, signature_constants as signature_constants, tag_constants as tag_constants
from tensorflow.python.training import saver as saver
from tensorflow.python.training.tracking import tracking as tracking
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

gen_trt_ops: Any

class TrtPrecisionMode:
    FP32: str
    FP16: str
    INT8: str
    @staticmethod
    def supported_precision_modes(): ...

DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES: Any
PROFILE_STRATEGY_RANGE: str
PROFILE_STRATEGY_OPTIMAL: str
PROFILE_STRATEGY_RANGE_OPTIMAL: str
PROFILE_STRATEGY_IMPLICIT_BATCH_MODE_COMPATIBLE: str

def supported_profile_strategies(): ...

class TrtConversionParams:
    def __new__(cls, max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = ..., maximum_cached_engines: int = ..., use_calibration: bool = ..., allow_build_at_runtime: bool = ...): ...

DEFAULT_TRT_CONVERSION_PARAMS: Any

def get_tensorrt_rewriter_config(conversion_params, is_dynamic_op: Any | None = ..., max_batch_size: Any | None = ..., is_v2: bool = ..., disable_non_trt_optimizers: bool = ...): ...

class TrtGraphConverter:
    def __init__(self, input_saved_model_dir: Any | None = ..., input_saved_model_tags: Any | None = ..., input_saved_model_signature_key: Any | None = ..., input_graph_def: Any | None = ..., nodes_denylist: Any | None = ..., max_batch_size: int = ..., max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = ..., is_dynamic_op: bool = ..., maximum_cached_engines: int = ..., use_calibration: bool = ...) -> None: ...
    def convert(self): ...
    def calibrate(self, fetch_names, num_runs, feed_dict_fn: Any | None = ..., input_map_fn: Any | None = ...): ...
    def save(self, output_saved_model_dir) -> None: ...

class _TRTEngineResource(tracking.TrackableResource):
    def __init__(self, resource_name, filename, maximum_cached_engines, device: str = ...) -> None: ...

class TrtGraphConverterV2:
    def __init__(self, input_saved_model_dir: Any | None = ..., input_saved_model_tags: Any | None = ..., input_saved_model_signature_key: Any | None = ..., use_dynamic_shape: Any | None = ..., dynamic_shape_profile_strategy: Any | None = ..., conversion_params: Any | None = ...) -> None: ...
    def convert(self, calibration_input_fn: Any | None = ...): ...
    def build(self, input_fn) -> None: ...
    def save(self, output_saved_model_dir) -> None: ...

def create_inference_graph(input_graph_def, outputs, max_batch_size: int = ..., max_workspace_size_bytes=..., precision_mode=..., minimum_segment_size: int = ..., is_dynamic_op: bool = ..., maximum_cached_engines: int = ..., input_saved_model_dir: Any | None = ..., input_saved_model_tags: Any | None = ..., input_saved_model_signature_key: Any | None = ..., output_saved_model_dir: Any | None = ...): ...

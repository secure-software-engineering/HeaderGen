from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python import pywrap_sanitizers as pywrap_sanitizers, tf2 as tf2
from tensorflow.python.client import device_lib as device_lib, pywrap_tf_session as pywrap_tf_session, session as session
from tensorflow.python.compat.compat import forward_compatibility_horizon as forward_compatibility_horizon
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function, tape as tape
from tensorflow.python.framework import config as config, dtypes as dtypes, errors as errors, errors_impl as errors_impl, gpu_util as gpu_util, importer as importer, ops as ops, random_seed as random_seed, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util, tfrt_utils as tfrt_utils, versions as versions
from tensorflow.python.framework.is_mlir_bridge_test_true import is_mlir_bridge_enabled as is_mlir_bridge_enabled
from tensorflow.python.framework.is_xla_test_true import is_xla_enabled as is_xla_enabled
from tensorflow.python.ops import array_ops as array_ops, control_flow_util as control_flow_util, control_flow_util_v2 as control_flow_util_v2, gradients_impl as gradients_impl, math_ops as math_ops, script_ops as script_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.ops.ragged import ragged_ops as ragged_ops, ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.platform import googletest as googletest
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import compat as compat, deprecation as deprecation, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect, traceback_utils as traceback_utils
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.protobuf import compare as compare
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

# def is_xla_enabled(): ...
# def is_mlir_bridge_enabled() -> None: ...
def is_asan_enabled(): ...
def is_msan_enabled(): ...
def is_tsan_enabled(): ...
def is_ubsan_enabled(): ...
def gpu_device_name(): ...
def assert_ops_in_graph(expected_ops, graph): ...
def assert_equal_graph_def_v2(expected, actual) -> None: ...
def assert_equal_graph_def_v1(actual, expected, checkpoint_v2: bool = ..., hash_table_shared_name: bool = ...) -> None: ...
def assert_equal_graph_def(actual, expected, checkpoint_v2: bool = ..., hash_table_shared_name: bool = ...) -> None: ...
def assert_meta_graph_protos_equal(tester, a, b) -> None: ...
def IsGoogleCudaEnabled(): ...
def IsBuiltWithROCm(): ...
def IsBuiltWithXLA(): ...
def IsBuiltWithNvcc(): ...
def GpuSupportsHalfMatMulAndConv(): ...
def IsMklEnabled(): ...
def InstallStackTraceHandler() -> None: ...
def NHWCToNCHW(input_tensor): ...
def NHWCToNCHW_VECT_C(input_shape_or_tensor): ...
def NCHW_VECT_CToNHWC(input_shape_or_tensor): ...
def NCHWToNHWC(input_tensor): ...
def skip_if(condition): ...
def skip_if_error(test_obj, error_type, messages: Any | None = ...) -> None: ...
def enable_c_shapes(fn): ...
def with_c_shapes(cls): ...
def enable_control_flow_v2(fn): ...
def with_control_flow_v2(cls): ...
def disable_control_flow_v2(unused_msg): ...
def enable_output_all_intermediates(fn): ...
def assert_no_new_pyobjects_executing_eagerly(func: Any | None = ..., warmup_iters: int = ...): ...
def assert_no_new_tensors(f): ...
def assert_no_garbage_created(f): ...
def generate_combinations_with_testcase_name(**kwargs): ...
def run_all_in_graph_and_eager_modes(cls): ...
def enable_eager_op_as_function(fn): ...
def with_eager_op_as_function(cls): ...
def disable_eager_op_as_function(unused_msg): ...
def build_as_function_and_v1_graph(func: Any | None = ...): ...
def run_in_async_and_sync_mode(f): ...
def run_in_graph_and_eager_modes(func: Any | None = ..., config: Any | None = ..., use_gpu: bool = ..., assert_no_eager_garbage: bool = ...): ...
def py_func_if_in_function(f): ...
def also_run_as_tf_function(f): ...
def deprecated_graph_mode_only(func: Any | None = ...): ...
run_deprecated_v1 = deprecated_graph_mode_only

def run_all_in_deprecated_graph_mode_only(cls): ...
def run_v1_only(reason, func: Any | None = ...): ...
def run_v2_only(func: Any | None = ...): ...
def run_gpu_only(func: Any | None = ...): ...
def run_cuda_only(func: Any | None = ...): ...
def run_gpu_or_tpu(func: Any | None = ...): ...
def with_forward_compatibility_horizons(*horizons): ...
def is_gpu_available(cuda_only: bool = ..., min_cuda_compute_capability: Any | None = ...): ...
def device(use_gpu) -> None: ...
def use_gpu() -> None: ...
def force_gpu() -> None: ...
def force_cpu() -> None: ...
def deterministic_ops() -> None: ...

class CapturedWrites:
    capture_location: Any
    def __init__(self, capture_location) -> None: ...
    def contents(self): ...

class FakeEagerSession:
    def __init__(self, test_case) -> None: ...
    def run(self, fetches, *args, **kwargs): ...

class ErrorLoggingSession(session.Session):
    def run(self, *args, **kwargs): ...

def disable_cudnn_autotune(func): ...
def enable_tf_xla_constant_folding(description): ...
def disable_xla(description): ...
def disable_mlir_bridge(description): ...
def disable_asan(description): ...
def disable_msan(description): ...
def disable_tsan(description): ...
def disable_ubsan(description): ...
def disable_tfrt(unused_description): ...
def for_all_test_methods(decorator, *args, **kwargs): ...
def no_xla_auto_jit(description): ...
def xla_allow_fallback(description): ...
def run_without_tensor_float_32(description): ...
def run_all_without_tensor_float_32(description): ...
def matmul_without_tf32(a, b, *args, **kwargs): ...

class EagerSessionWarner:
    def __getattr__(self, attr) -> None: ...

class TensorFlowTestCase(googletest.TestCase):
    def __init__(self, methodName: str = ...) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def get_temp_dir(self): ...
    def captureWritesToStream(self, stream) -> None: ...
    def assertProtoEquals(self, expected_message_maybe_ascii, message, msg: Any | None = ...) -> None: ...
    def assertProtoEqualsVersion(self, expected, actual, producer=..., min_consumer=..., msg: Any | None = ...) -> None: ...
    def assertStartsWith(self, actual, expected_start, msg: Any | None = ...) -> None: ...
    def evaluate(self, tensors): ...
    def session(self, graph: Any | None = ..., config: Any | None = ..., use_gpu: bool = ..., force_gpu: bool = ...) -> None: ...
    def cached_session(self, graph: Any | None = ..., config: Any | None = ..., use_gpu: bool = ..., force_gpu: bool = ...) -> None: ...
    def test_session(self, graph: Any | None = ..., config: Any | None = ..., use_gpu: bool = ..., force_gpu: bool = ...) -> None: ...
    class _CheckedThread:
        def __init__(self, testcase, target, args: Any | None = ..., kwargs: Any | None = ...) -> None: ...
        def start(self) -> None: ...
        def join(self) -> None: ...
        def is_alive(self): ...
        def check_termination(self) -> None: ...
    def checkedThread(self, target, args: Any | None = ..., kwargs: Any | None = ...): ...
    def assertNear(self, f1, f2, err, msg: Any | None = ...) -> None: ...
    def assertArrayNear(self, farray1, farray2, err, msg: Any | None = ...) -> None: ...
    def assertNDArrayNear(self, ndarray1, ndarray2, err, msg: Any | None = ...) -> None: ...
    def evaluate_if_both_tensors(self, a, b): ...
    def assertAllClose(self, a, b, rtol: float = ..., atol: float = ..., msg: Any | None = ...): ...
    def assertAllCloseAccordingToType(self, a, b, rtol: float = ..., atol: float = ..., float_rtol: float = ..., float_atol: float = ..., half_rtol: float = ..., half_atol: float = ..., bfloat16_rtol: float = ..., bfloat16_atol: float = ..., msg: Any | None = ...) -> None: ...
    def assertNotAllClose(self, a, b, rtol: float = ..., atol: float = ..., msg: Any | None = ...) -> None: ...
    def assertAllEqual(self, a, b, msg: Any | None = ...): ...
    def assertNotAllEqual(self, a, b, msg: Any | None = ...) -> None: ...
    def assertAllGreater(self, a, comparison_target) -> None: ...
    def assertAllLess(self, a, comparison_target) -> None: ...
    def assertAllGreaterEqual(self, a, comparison_target) -> None: ...
    def assertAllLessEqual(self, a, comparison_target) -> None: ...
    def assertAllInRange(self, target, lower_bound, upper_bound, open_lower_bound: bool = ..., open_upper_bound: bool = ...) -> None: ...
    def assertAllInSet(self, target, expected_set) -> None: ...
    def assertDTypeEqual(self, target, expected_dtype) -> None: ...
    def assertRaisesWithPredicateMatch(self, exception_type, expected_err_re_or_predicate): ...
    def assertRaisesOpError(self, expected_err_re_or_predicate): ...
    def assertRaisesIncompatibleShapesError(self, exception_type=...): ...
    def assertShapeEqual(self, np_array, tf_tensor, msg: Any | None = ...) -> None: ...
    def assertDeviceEqual(self, device1, device2, msg: Any | None = ...) -> None: ...
    assertRaisesRegexp: Any
    assertItemsEqual: Any

def create_local_cluster(num_workers, num_ps, protocol: str = ..., worker_config: Any | None = ..., ps_config: Any | None = ...): ...
def get_node_def_from_graph(node_name, graph_def): ...
def set_producer_version(graph, producer_version) -> None: ...

class AbstractGradientTape:
    def __init__(self, use_tape, persistent: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

def run_functions_eagerly(run_eagerly) -> None: ...

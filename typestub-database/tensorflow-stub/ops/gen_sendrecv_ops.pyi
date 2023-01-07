from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def recv(tensor_type, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated: bool = ..., name: Any | None = ...): ...

Recv: Any

def recv_eager_fallback(tensor_type, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated, name, ctx): ...
def send(tensor, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated: bool = ..., name: Any | None = ...): ...

Send: Any

def send_eager_fallback(tensor, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated, name, ctx): ...

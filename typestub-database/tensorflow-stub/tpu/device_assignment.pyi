import enum
import numpy as np
from tensorflow.python.tpu.topology import Topology as Topology
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, List, Optional, Text, Tuple

SINGLE_CORE_ASSIGNMENT: Any

class DeviceAssignment:
    def __init__(self, topology: Topology, core_assignment: np.ndarray) -> None: ...
    @property
    def topology(self) -> Topology: ...
    @property
    def num_cores_per_replica(self) -> int: ...
    @property
    def num_replicas(self) -> int: ...
    @property
    def core_assignment(self) -> np.ndarray: ...
    def coordinates(self, replica: int, logical_core: int) -> Tuple: ...
    def lookup_replicas(self, task_id: int, logical_core: int) -> List[int]: ...
    def tpu_ordinal(self, replica: int = ..., logical_core: int = ...) -> int: ...
    def host_device(self, replica: int = ..., logical_core: int = ..., job: Optional[Text] = ...) -> Text: ...
    def tpu_device(self, replica: int = ..., logical_core: int = ..., job: Optional[Text] = ...) -> Text: ...
    @staticmethod
    def build(topology: Topology, computation_shape: Optional[np.ndarray] = ..., computation_stride: Optional[np.ndarray] = ..., num_replicas: int = ...) -> DeviceAssignment: ...

class DeviceOrderMode(enum.IntEnum):
    AUTO: int
    RING: int
    MESH: int

def device_assignment(topology: Topology, computation_shape: Optional[np.ndarray] = ..., computation_stride: Optional[np.ndarray] = ..., num_replicas: int = ..., device_order_mode: DeviceOrderMode = ...) -> DeviceAssignment: ...

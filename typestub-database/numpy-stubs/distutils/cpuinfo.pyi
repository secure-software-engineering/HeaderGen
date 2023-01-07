from typing import Any

class CPUInfoBase:
    def __getattr__(self, name): ...

class LinuxCPUInfo(CPUInfoBase):
    info: Any
    def __init__(self) -> None: ...

class IRIXCPUInfo(CPUInfoBase):
    info: Any
    def __init__(self) -> None: ...
    def get_ip(self): ...

class DarwinCPUInfo(CPUInfoBase):
    info: Any
    def __init__(self) -> None: ...

class SunOSCPUInfo(CPUInfoBase):
    info: Any
    def __init__(self) -> None: ...

class Win32CPUInfo(CPUInfoBase):
    info: Any
    pkey: str
    def __init__(self) -> None: ...
cpuinfo = LinuxCPUInfo
cpu: Any

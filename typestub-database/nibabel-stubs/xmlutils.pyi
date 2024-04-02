from xml.etree.ElementTree import SubElement as SubElement

from _typeshed import Incomplete

from .filebasedimages import FileBasedHeader as FileBasedHeader

class XmlSerializable:
    def to_xml(self, enc: str = "utf-8", **kwargs) -> bytes: ...

class XmlBasedHeader(FileBasedHeader, XmlSerializable): ...

class XmlParser:
    HANDLER_NAMES: Incomplete
    encoding: Incomplete
    buffer_size: Incomplete
    verbose: Incomplete
    fname: Incomplete
    def __init__(
        self, encoding: str = "utf-8", buffer_size: int = 35000000, verbose: int = 0
    ) -> None: ...
    def parse(
        self,
        string: Incomplete | None = None,
        fname: Incomplete | None = None,
        fptr: Incomplete | None = None,
    ) -> None: ...
    def StartElementHandler(self, name, attrs) -> None: ...
    def EndElementHandler(self, name) -> None: ...
    def CharacterDataHandler(self, data) -> None: ...

from numpy import complexfloating as complexfloating, floating as floating, generic as generic, signedinteger as signedinteger, unsignedinteger as unsignedinteger
from typing import Dict, List, Type, Union
from typing_extensions import TypedDict

class _SCTypes(TypedDict):
    int: List[Type[signedinteger]]
    uint: List[Type[unsignedinteger]]
    float: List[Type[floating]]
    complex: List[Type[complexfloating]]
    others: List[type]

sctypeDict: Dict[Union[int, str], Type[generic]]
sctypes: _SCTypes

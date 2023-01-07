from sklearn.linear_model._glm.link import IdentityLink as IdentityLink, LogLink as LogLink, LogitLink as LogitLink
from typing import Any

LINK_FUNCTIONS: Any

def test_link_properties(Link) -> None: ...
def test_link_derivative(Link) -> None: ...

from tensorflow.python.autograph.core import config as config
from tensorflow.python.autograph.pyct import cache as cache, inspect_utils as inspect_utils
from tensorflow.python.eager import function as function
from tensorflow.python.util import tf_inspect as tf_inspect

def is_unsupported(o): ...
def is_allowlisted(o, check_call_override: bool = ..., allow_namedtuple_subclass: bool = ...): ...
def is_in_allowlist_cache(entity, options): ...
def cache_allowlisted(entity, options) -> None: ...

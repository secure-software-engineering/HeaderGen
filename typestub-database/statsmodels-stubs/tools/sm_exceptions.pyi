class PerfectSeparationError(Exception): ...
class MissingDataError(Exception): ...
class X13NotFoundError(Exception): ...
class X13Error(Exception): ...
class ParseError(Exception): ...
class X13Warning(Warning): ...
class IOWarning(RuntimeWarning): ...
class ModuleUnavailableWarning(Warning): ...

module_unavailable_doc: str

class ModelWarning(UserWarning): ...
class ConvergenceWarning(ModelWarning): ...

convergence_doc: str

class CacheWriteWarning(ModelWarning): ...
class IterationLimitWarning(ModelWarning): ...

iteration_limit_doc: str

class InvalidTestWarning(ModelWarning): ...
class NotImplementedWarning(ModelWarning): ...
class OutputWarning(ModelWarning): ...
class DomainWarning(ModelWarning): ...
class ValueWarning(ModelWarning): ...
class EstimationWarning(ModelWarning): ...
class SingularMatrixWarning(ModelWarning): ...
class HypothesisTestWarning(ModelWarning): ...
class InterpolationWarning(ModelWarning): ...
class PrecisionWarning(ModelWarning): ...
class SpecificationWarning(ModelWarning): ...
class HessianInversionWarning(ModelWarning): ...
class CollinearityWarning(ModelWarning): ...
class InfeasibleTestError(RuntimeError): ...

recarray_exception: str

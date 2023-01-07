from ._analytic_rotation import target_rotation as target_rotation
from ._gpa_rotation import CF_objective as CF_objective, GPA as GPA, ff_partial_target as ff_partial_target, ff_target as ff_target, oblimin_objective as oblimin_objective, orthomax_objective as orthomax_objective, rotateA as rotateA, vgQ_partial_target as vgQ_partial_target, vgQ_target as vgQ_target

def rotate_factors(A, method, *method_args, **algorithm_kwargs): ...

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1429 import AGMA6123SplineJointDutyCycleRating
    from ._1430 import GBT17855SplineJointDutyCycleRating
    from ._1431 import SAESplineJointDutyCycleRating
else:
    import_structure = {
        "_1429": ["AGMA6123SplineJointDutyCycleRating"],
        "_1430": ["GBT17855SplineJointDutyCycleRating"],
        "_1431": ["SAESplineJointDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineJointDutyCycleRating",
    "GBT17855SplineJointDutyCycleRating",
    "SAESplineJointDutyCycleRating",
)

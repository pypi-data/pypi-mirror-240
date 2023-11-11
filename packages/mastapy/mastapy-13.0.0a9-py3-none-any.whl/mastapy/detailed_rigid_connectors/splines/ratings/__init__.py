"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1419 import AGMA6123SplineHalfRating
    from ._1420 import AGMA6123SplineJointRating
    from ._1421 import DIN5466SplineHalfRating
    from ._1422 import DIN5466SplineRating
    from ._1423 import GBT17855SplineHalfRating
    from ._1424 import GBT17855SplineJointRating
    from ._1425 import SAESplineHalfRating
    from ._1426 import SAESplineJointRating
    from ._1427 import SplineHalfRating
    from ._1428 import SplineJointRating
else:
    import_structure = {
        "_1419": ["AGMA6123SplineHalfRating"],
        "_1420": ["AGMA6123SplineJointRating"],
        "_1421": ["DIN5466SplineHalfRating"],
        "_1422": ["DIN5466SplineRating"],
        "_1423": ["GBT17855SplineHalfRating"],
        "_1424": ["GBT17855SplineJointRating"],
        "_1425": ["SAESplineHalfRating"],
        "_1426": ["SAESplineJointRating"],
        "_1427": ["SplineHalfRating"],
        "_1428": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)

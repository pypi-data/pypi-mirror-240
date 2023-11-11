"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5519 import AbstractMeasuredDynamicResponseAtTime
    from ._5520 import DynamicForceResultAtTime
    from ._5521 import DynamicForceVector3DResult
    from ._5522 import DynamicTorqueResultAtTime
    from ._5523 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5519": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5520": ["DynamicForceResultAtTime"],
        "_5521": ["DynamicForceVector3DResult"],
        "_5522": ["DynamicTorqueResultAtTime"],
        "_5523": ["DynamicTorqueVector3DResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
)

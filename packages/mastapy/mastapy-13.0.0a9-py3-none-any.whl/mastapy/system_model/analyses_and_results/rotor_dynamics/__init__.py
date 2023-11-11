"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4023 import RotorDynamicsDrawStyle
    from ._4024 import ShaftComplexShape
    from ._4025 import ShaftForcedComplexShape
    from ._4026 import ShaftModalComplexShape
    from ._4027 import ShaftModalComplexShapeAtSpeeds
    from ._4028 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4023": ["RotorDynamicsDrawStyle"],
        "_4024": ["ShaftComplexShape"],
        "_4025": ["ShaftForcedComplexShape"],
        "_4026": ["ShaftModalComplexShape"],
        "_4027": ["ShaftModalComplexShapeAtSpeeds"],
        "_4028": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)

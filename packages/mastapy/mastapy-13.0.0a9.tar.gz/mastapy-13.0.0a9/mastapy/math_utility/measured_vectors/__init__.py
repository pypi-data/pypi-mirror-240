"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1556 import AbstractForceAndDisplacementResults
    from ._1557 import ForceAndDisplacementResults
    from ._1558 import ForceResults
    from ._1559 import NodeResults
    from ._1560 import OverridableDisplacementBoundaryCondition
    from ._1561 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1556": ["AbstractForceAndDisplacementResults"],
        "_1557": ["ForceAndDisplacementResults"],
        "_1558": ["ForceResults"],
        "_1559": ["NodeResults"],
        "_1560": ["OverridableDisplacementBoundaryCondition"],
        "_1561": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)

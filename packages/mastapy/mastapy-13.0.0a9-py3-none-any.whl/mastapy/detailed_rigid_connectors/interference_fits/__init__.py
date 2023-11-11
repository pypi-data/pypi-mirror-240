"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1439 import AssemblyMethods
    from ._1440 import CalculationMethods
    from ._1441 import InterferenceFitDesign
    from ._1442 import InterferenceFitHalfDesign
    from ._1443 import StressRegions
    from ._1444 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1439": ["AssemblyMethods"],
        "_1440": ["CalculationMethods"],
        "_1441": ["InterferenceFitDesign"],
        "_1442": ["InterferenceFitHalfDesign"],
        "_1443": ["StressRegions"],
        "_1444": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)

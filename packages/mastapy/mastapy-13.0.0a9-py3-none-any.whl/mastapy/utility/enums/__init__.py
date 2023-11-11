"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1816 import BearingForceArrowOption
    from ._1817 import TableAndChartOptions
    from ._1818 import ThreeDViewContourOption
    from ._1819 import ThreeDViewContourOptionFirstSelection
    from ._1820 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1816": ["BearingForceArrowOption"],
        "_1817": ["TableAndChartOptions"],
        "_1818": ["ThreeDViewContourOption"],
        "_1819": ["ThreeDViewContourOptionFirstSelection"],
        "_1820": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)

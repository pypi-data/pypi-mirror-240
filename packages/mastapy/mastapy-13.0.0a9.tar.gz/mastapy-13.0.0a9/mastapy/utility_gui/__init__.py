"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1844 import ColumnInputOptions
    from ._1845 import DataInputFileOptions
    from ._1846 import DataLoggerItem
    from ._1847 import DataLoggerWithCharts
    from ._1848 import ScalingDrawStyle
else:
    import_structure = {
        "_1844": ["ColumnInputOptions"],
        "_1845": ["DataInputFileOptions"],
        "_1846": ["DataLoggerItem"],
        "_1847": ["DataLoggerWithCharts"],
        "_1848": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)

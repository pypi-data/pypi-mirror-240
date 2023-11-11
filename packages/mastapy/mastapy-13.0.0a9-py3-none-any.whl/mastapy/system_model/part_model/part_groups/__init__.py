"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2483 import ConcentricOrParallelPartGroup
    from ._2484 import ConcentricPartGroup
    from ._2485 import ConcentricPartGroupParallelToThis
    from ._2486 import DesignMeasurements
    from ._2487 import ParallelPartGroup
    from ._2488 import ParallelPartGroupSelection
    from ._2489 import PartGroup
else:
    import_structure = {
        "_2483": ["ConcentricOrParallelPartGroup"],
        "_2484": ["ConcentricPartGroup"],
        "_2485": ["ConcentricPartGroupParallelToThis"],
        "_2486": ["DesignMeasurements"],
        "_2487": ["ParallelPartGroup"],
        "_2488": ["ParallelPartGroupSelection"],
        "_2489": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2481 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2482 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        "_2481": ["SpecifiedConcentricPartGroupDrawingOrder"],
        "_2482": ["SpecifiedParallelPartGroupDrawingOrder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpecifiedConcentricPartGroupDrawingOrder",
    "SpecifiedParallelPartGroupDrawingOrder",
)

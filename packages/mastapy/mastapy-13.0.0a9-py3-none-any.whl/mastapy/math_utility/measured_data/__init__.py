"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1562 import GriddedSurfaceAccessor
    from ._1563 import LookupTableBase
    from ._1564 import OnedimensionalFunctionLookupTable
    from ._1565 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1562": ["GriddedSurfaceAccessor"],
        "_1563": ["LookupTableBase"],
        "_1564": ["OnedimensionalFunctionLookupTable"],
        "_1565": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)

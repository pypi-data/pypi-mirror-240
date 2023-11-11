"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1571 import ConvergenceLogger
    from ._1572 import DataLogger
else:
    import_structure = {
        "_1571": ["ConvergenceLogger"],
        "_1572": ["DataLogger"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConvergenceLogger",
    "DataLogger",
)

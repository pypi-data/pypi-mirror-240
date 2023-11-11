"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1814 import ColumnTitle
    from ._1815 import TextFileDelimiterOptions
else:
    import_structure = {
        "_1814": ["ColumnTitle"],
        "_1815": ["TextFileDelimiterOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnTitle",
    "TextFileDelimiterOptions",
)

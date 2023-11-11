"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1788 import Fix
    from ._1789 import Severity
    from ._1790 import Status
    from ._1791 import StatusItem
    from ._1792 import StatusItemSeverity
else:
    import_structure = {
        "_1788": ["Fix"],
        "_1789": ["Severity"],
        "_1790": ["Status"],
        "_1791": ["StatusItem"],
        "_1792": ["StatusItemSeverity"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
)

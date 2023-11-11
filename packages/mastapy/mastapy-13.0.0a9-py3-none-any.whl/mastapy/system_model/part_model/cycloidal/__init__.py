"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2565 import CycloidalAssembly
    from ._2566 import CycloidalDisc
    from ._2567 import RingPins
else:
    import_structure = {
        "_2565": ["CycloidalAssembly"],
        "_2566": ["CycloidalDisc"],
        "_2567": ["RingPins"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalAssembly",
    "CycloidalDisc",
    "RingPins",
)

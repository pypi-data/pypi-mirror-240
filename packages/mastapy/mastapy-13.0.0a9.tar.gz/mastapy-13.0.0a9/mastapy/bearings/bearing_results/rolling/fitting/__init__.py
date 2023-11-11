"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2107 import InnerRingFittingThermalResults
    from ._2108 import InterferenceComponents
    from ._2109 import OuterRingFittingThermalResults
    from ._2110 import RingFittingThermalResults
else:
    import_structure = {
        "_2107": ["InnerRingFittingThermalResults"],
        "_2108": ["InterferenceComponents"],
        "_2109": ["OuterRingFittingThermalResults"],
        "_2110": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)

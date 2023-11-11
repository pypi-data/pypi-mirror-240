"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2234 import DesignStateTargetRatio
    from ._2235 import PlanetGearOptions
    from ._2236 import SystemOptimiser
    from ._2237 import SystemOptimiserDetails
    from ._2238 import ToothNumberFinder
else:
    import_structure = {
        "_2234": ["DesignStateTargetRatio"],
        "_2235": ["PlanetGearOptions"],
        "_2236": ["SystemOptimiser"],
        "_2237": ["SystemOptimiserDetails"],
        "_2238": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)

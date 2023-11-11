"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2127 import BearingDesign
    from ._2128 import DetailedBearing
    from ._2129 import DummyRollingBearing
    from ._2130 import LinearBearing
    from ._2131 import NonLinearBearing
else:
    import_structure = {
        "_2127": ["BearingDesign"],
        "_2128": ["DetailedBearing"],
        "_2129": ["DummyRollingBearing"],
        "_2130": ["LinearBearing"],
        "_2131": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)

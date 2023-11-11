"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1533 import IndividualContactPosition
    from ._1534 import SurfaceToSurfaceContact
else:
    import_structure = {
        "_1533": ["IndividualContactPosition"],
        "_1534": ["SurfaceToSurfaceContact"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "IndividualContactPosition",
    "SurfaceToSurfaceContact",
)

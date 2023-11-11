"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2563 import GearMaterialExpertSystemMaterialDetails
    from ._2564 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        "_2563": ["GearMaterialExpertSystemMaterialDetails"],
        "_2564": ["GearMaterialExpertSystemMaterialOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMaterialExpertSystemMaterialDetails",
    "GearMaterialExpertSystemMaterialOptions",
)

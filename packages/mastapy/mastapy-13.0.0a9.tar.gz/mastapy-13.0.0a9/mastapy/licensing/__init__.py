"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1484 import LicenceServer
    from ._7568 import LicenceServerDetails
    from ._7569 import ModuleDetails
    from ._7570 import ModuleLicenceStatus
else:
    import_structure = {
        "_1484": ["LicenceServer"],
        "_7568": ["LicenceServerDetails"],
        "_7569": ["ModuleDetails"],
        "_7570": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)

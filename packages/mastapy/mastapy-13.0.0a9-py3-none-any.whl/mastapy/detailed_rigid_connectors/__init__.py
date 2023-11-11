"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1383 import DetailedRigidConnectorDesign
    from ._1384 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1383": ["DetailedRigidConnectorDesign"],
        "_1384": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)

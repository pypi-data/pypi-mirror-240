"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1433 import KeyedJointDesign
    from ._1434 import KeyTypes
    from ._1435 import KeywayJointHalfDesign
    from ._1436 import NumberOfKeys
else:
    import_structure = {
        "_1433": ["KeyedJointDesign"],
        "_1434": ["KeyTypes"],
        "_1435": ["KeywayJointHalfDesign"],
        "_1436": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)

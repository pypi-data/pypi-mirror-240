"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1794 import GearMeshForTE
    from ._1795 import GearOrderForTE
    from ._1796 import GearPositions
    from ._1797 import HarmonicOrderForTE
    from ._1798 import LabelOnlyOrder
    from ._1799 import OrderForTE
    from ._1800 import OrderSelector
    from ._1801 import OrderWithRadius
    from ._1802 import RollingBearingOrder
    from ._1803 import ShaftOrderForTE
    from ._1804 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1794": ["GearMeshForTE"],
        "_1795": ["GearOrderForTE"],
        "_1796": ["GearPositions"],
        "_1797": ["HarmonicOrderForTE"],
        "_1798": ["LabelOnlyOrder"],
        "_1799": ["OrderForTE"],
        "_1800": ["OrderSelector"],
        "_1801": ["OrderWithRadius"],
        "_1802": ["RollingBearingOrder"],
        "_1803": ["ShaftOrderForTE"],
        "_1804": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)

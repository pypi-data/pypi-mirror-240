"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2568 import BeltCreationOptions
    from ._2569 import CycloidalAssemblyCreationOptions
    from ._2570 import CylindricalGearLinearTrainCreationOptions
    from ._2571 import PlanetCarrierCreationOptions
    from ._2572 import ShaftCreationOptions
else:
    import_structure = {
        "_2568": ["BeltCreationOptions"],
        "_2569": ["CycloidalAssemblyCreationOptions"],
        "_2570": ["CylindricalGearLinearTrainCreationOptions"],
        "_2571": ["PlanetCarrierCreationOptions"],
        "_2572": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)

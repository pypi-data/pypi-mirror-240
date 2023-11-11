"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2490 import AbstractShaftFromCAD
    from ._2491 import ClutchFromCAD
    from ._2492 import ComponentFromCAD
    from ._2493 import ConceptBearingFromCAD
    from ._2494 import ConnectorFromCAD
    from ._2495 import CylindricalGearFromCAD
    from ._2496 import CylindricalGearInPlanetarySetFromCAD
    from ._2497 import CylindricalPlanetGearFromCAD
    from ._2498 import CylindricalRingGearFromCAD
    from ._2499 import CylindricalSunGearFromCAD
    from ._2500 import HousedOrMounted
    from ._2501 import MountableComponentFromCAD
    from ._2502 import PlanetShaftFromCAD
    from ._2503 import PulleyFromCAD
    from ._2504 import RigidConnectorFromCAD
    from ._2505 import RollingBearingFromCAD
    from ._2506 import ShaftFromCAD
else:
    import_structure = {
        "_2490": ["AbstractShaftFromCAD"],
        "_2491": ["ClutchFromCAD"],
        "_2492": ["ComponentFromCAD"],
        "_2493": ["ConceptBearingFromCAD"],
        "_2494": ["ConnectorFromCAD"],
        "_2495": ["CylindricalGearFromCAD"],
        "_2496": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2497": ["CylindricalPlanetGearFromCAD"],
        "_2498": ["CylindricalRingGearFromCAD"],
        "_2499": ["CylindricalSunGearFromCAD"],
        "_2500": ["HousedOrMounted"],
        "_2501": ["MountableComponentFromCAD"],
        "_2502": ["PlanetShaftFromCAD"],
        "_2503": ["PulleyFromCAD"],
        "_2504": ["RigidConnectorFromCAD"],
        "_2505": ["RollingBearingFromCAD"],
        "_2506": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)

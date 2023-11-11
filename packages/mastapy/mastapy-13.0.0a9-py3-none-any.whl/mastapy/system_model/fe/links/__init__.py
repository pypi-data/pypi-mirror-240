"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2415 import FELink
    from ._2416 import ElectricMachineStatorFELink
    from ._2417 import FELinkWithSelection
    from ._2418 import GearMeshFELink
    from ._2419 import GearWithDuplicatedMeshesFELink
    from ._2420 import MultiAngleConnectionFELink
    from ._2421 import MultiNodeConnectorFELink
    from ._2422 import MultiNodeFELink
    from ._2423 import PlanetaryConnectorMultiNodeFELink
    from ._2424 import PlanetBasedFELink
    from ._2425 import PlanetCarrierFELink
    from ._2426 import PointLoadFELink
    from ._2427 import RollingRingConnectionFELink
    from ._2428 import ShaftHubConnectionFELink
    from ._2429 import SingleNodeFELink
else:
    import_structure = {
        "_2415": ["FELink"],
        "_2416": ["ElectricMachineStatorFELink"],
        "_2417": ["FELinkWithSelection"],
        "_2418": ["GearMeshFELink"],
        "_2419": ["GearWithDuplicatedMeshesFELink"],
        "_2420": ["MultiAngleConnectionFELink"],
        "_2421": ["MultiNodeConnectorFELink"],
        "_2422": ["MultiNodeFELink"],
        "_2423": ["PlanetaryConnectorMultiNodeFELink"],
        "_2424": ["PlanetBasedFELink"],
        "_2425": ["PlanetCarrierFELink"],
        "_2426": ["PointLoadFELink"],
        "_2427": ["RollingRingConnectionFELink"],
        "_2428": ["ShaftHubConnectionFELink"],
        "_2429": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)

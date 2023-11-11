"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2573 import BeltDrive
    from ._2574 import BeltDriveType
    from ._2575 import Clutch
    from ._2576 import ClutchHalf
    from ._2577 import ClutchType
    from ._2578 import ConceptCoupling
    from ._2579 import ConceptCouplingHalf
    from ._2580 import Coupling
    from ._2581 import CouplingHalf
    from ._2582 import CrowningSpecification
    from ._2583 import CVT
    from ._2584 import CVTPulley
    from ._2585 import PartToPartShearCoupling
    from ._2586 import PartToPartShearCouplingHalf
    from ._2587 import Pulley
    from ._2588 import RigidConnectorStiffnessType
    from ._2589 import RigidConnectorTiltStiffnessTypes
    from ._2590 import RigidConnectorToothLocation
    from ._2591 import RigidConnectorToothSpacingType
    from ._2592 import RigidConnectorTypes
    from ._2593 import RollingRing
    from ._2594 import RollingRingAssembly
    from ._2595 import ShaftHubConnection
    from ._2596 import SplineLeadRelief
    from ._2597 import SpringDamper
    from ._2598 import SpringDamperHalf
    from ._2599 import Synchroniser
    from ._2600 import SynchroniserCone
    from ._2601 import SynchroniserHalf
    from ._2602 import SynchroniserPart
    from ._2603 import SynchroniserSleeve
    from ._2604 import TorqueConverter
    from ._2605 import TorqueConverterPump
    from ._2606 import TorqueConverterSpeedRatio
    from ._2607 import TorqueConverterTurbine
else:
    import_structure = {
        "_2573": ["BeltDrive"],
        "_2574": ["BeltDriveType"],
        "_2575": ["Clutch"],
        "_2576": ["ClutchHalf"],
        "_2577": ["ClutchType"],
        "_2578": ["ConceptCoupling"],
        "_2579": ["ConceptCouplingHalf"],
        "_2580": ["Coupling"],
        "_2581": ["CouplingHalf"],
        "_2582": ["CrowningSpecification"],
        "_2583": ["CVT"],
        "_2584": ["CVTPulley"],
        "_2585": ["PartToPartShearCoupling"],
        "_2586": ["PartToPartShearCouplingHalf"],
        "_2587": ["Pulley"],
        "_2588": ["RigidConnectorStiffnessType"],
        "_2589": ["RigidConnectorTiltStiffnessTypes"],
        "_2590": ["RigidConnectorToothLocation"],
        "_2591": ["RigidConnectorToothSpacingType"],
        "_2592": ["RigidConnectorTypes"],
        "_2593": ["RollingRing"],
        "_2594": ["RollingRingAssembly"],
        "_2595": ["ShaftHubConnection"],
        "_2596": ["SplineLeadRelief"],
        "_2597": ["SpringDamper"],
        "_2598": ["SpringDamperHalf"],
        "_2599": ["Synchroniser"],
        "_2600": ["SynchroniserCone"],
        "_2601": ["SynchroniserHalf"],
        "_2602": ["SynchroniserPart"],
        "_2603": ["SynchroniserSleeve"],
        "_2604": ["TorqueConverter"],
        "_2605": ["TorqueConverterPump"],
        "_2606": ["TorqueConverterSpeedRatio"],
        "_2607": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineLeadRelief",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)

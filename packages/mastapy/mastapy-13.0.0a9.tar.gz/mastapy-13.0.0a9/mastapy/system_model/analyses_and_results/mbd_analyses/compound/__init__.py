"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5525 import AbstractAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5526 import AbstractShaftCompoundMultibodyDynamicsAnalysis
    from ._5527 import AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
    from ._5528 import (
        AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5529 import AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5530 import AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5531 import AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5532 import AssemblyCompoundMultibodyDynamicsAnalysis
    from ._5533 import BearingCompoundMultibodyDynamicsAnalysis
    from ._5534 import BeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5535 import BeltDriveCompoundMultibodyDynamicsAnalysis
    from ._5536 import BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
    from ._5537 import BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5538 import BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
    from ._5539 import BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5540 import BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
    from ._5541 import BevelGearCompoundMultibodyDynamicsAnalysis
    from ._5542 import BevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5543 import BevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5544 import BoltCompoundMultibodyDynamicsAnalysis
    from ._5545 import BoltedJointCompoundMultibodyDynamicsAnalysis
    from ._5546 import ClutchCompoundMultibodyDynamicsAnalysis
    from ._5547 import ClutchConnectionCompoundMultibodyDynamicsAnalysis
    from ._5548 import ClutchHalfCompoundMultibodyDynamicsAnalysis
    from ._5549 import CoaxialConnectionCompoundMultibodyDynamicsAnalysis
    from ._5550 import ComponentCompoundMultibodyDynamicsAnalysis
    from ._5551 import ConceptCouplingCompoundMultibodyDynamicsAnalysis
    from ._5552 import ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5553 import ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5554 import ConceptGearCompoundMultibodyDynamicsAnalysis
    from ._5555 import ConceptGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5556 import ConceptGearSetCompoundMultibodyDynamicsAnalysis
    from ._5557 import ConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5558 import ConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5559 import ConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5560 import ConnectionCompoundMultibodyDynamicsAnalysis
    from ._5561 import ConnectorCompoundMultibodyDynamicsAnalysis
    from ._5562 import CouplingCompoundMultibodyDynamicsAnalysis
    from ._5563 import CouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5564 import CouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5565 import CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5566 import CVTCompoundMultibodyDynamicsAnalysis
    from ._5567 import CVTPulleyCompoundMultibodyDynamicsAnalysis
    from ._5568 import CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5569 import (
        CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5570 import CycloidalDiscCompoundMultibodyDynamicsAnalysis
    from ._5571 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5572 import CylindricalGearCompoundMultibodyDynamicsAnalysis
    from ._5573 import CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5574 import CylindricalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5575 import CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5576 import DatumCompoundMultibodyDynamicsAnalysis
    from ._5577 import ExternalCADModelCompoundMultibodyDynamicsAnalysis
    from ._5578 import FaceGearCompoundMultibodyDynamicsAnalysis
    from ._5579 import FaceGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5580 import FaceGearSetCompoundMultibodyDynamicsAnalysis
    from ._5581 import FEPartCompoundMultibodyDynamicsAnalysis
    from ._5582 import FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5583 import GearCompoundMultibodyDynamicsAnalysis
    from ._5584 import GearMeshCompoundMultibodyDynamicsAnalysis
    from ._5585 import GearSetCompoundMultibodyDynamicsAnalysis
    from ._5586 import GuideDxfModelCompoundMultibodyDynamicsAnalysis
    from ._5587 import HypoidGearCompoundMultibodyDynamicsAnalysis
    from ._5588 import HypoidGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5589 import HypoidGearSetCompoundMultibodyDynamicsAnalysis
    from ._5590 import (
        InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5591 import (
        KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5592 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5593 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5594 import (
        KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5595 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5596 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5597 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5598 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5599 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5600 import MassDiscCompoundMultibodyDynamicsAnalysis
    from ._5601 import MeasurementComponentCompoundMultibodyDynamicsAnalysis
    from ._5602 import MountableComponentCompoundMultibodyDynamicsAnalysis
    from ._5603 import OilSealCompoundMultibodyDynamicsAnalysis
    from ._5604 import PartCompoundMultibodyDynamicsAnalysis
    from ._5605 import PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
    from ._5606 import (
        PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5607 import PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5608 import PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
    from ._5609 import PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
    from ._5610 import PlanetCarrierCompoundMultibodyDynamicsAnalysis
    from ._5611 import PointLoadCompoundMultibodyDynamicsAnalysis
    from ._5612 import PowerLoadCompoundMultibodyDynamicsAnalysis
    from ._5613 import PulleyCompoundMultibodyDynamicsAnalysis
    from ._5614 import RingPinsCompoundMultibodyDynamicsAnalysis
    from ._5615 import RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
    from ._5616 import RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5617 import RollingRingCompoundMultibodyDynamicsAnalysis
    from ._5618 import RollingRingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5619 import RootAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5620 import ShaftCompoundMultibodyDynamicsAnalysis
    from ._5621 import ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
    from ._5622 import (
        ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5623 import SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5624 import SpiralBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5625 import SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5626 import SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5627 import SpringDamperCompoundMultibodyDynamicsAnalysis
    from ._5628 import SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
    from ._5629 import SpringDamperHalfCompoundMultibodyDynamicsAnalysis
    from ._5630 import StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
    from ._5631 import StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5632 import StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
    from ._5633 import StraightBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5634 import StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5635 import StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5636 import StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5637 import StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
    from ._5638 import SynchroniserCompoundMultibodyDynamicsAnalysis
    from ._5639 import SynchroniserHalfCompoundMultibodyDynamicsAnalysis
    from ._5640 import SynchroniserPartCompoundMultibodyDynamicsAnalysis
    from ._5641 import SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
    from ._5642 import TorqueConverterCompoundMultibodyDynamicsAnalysis
    from ._5643 import TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
    from ._5644 import TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
    from ._5645 import TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
    from ._5646 import UnbalancedMassCompoundMultibodyDynamicsAnalysis
    from ._5647 import VirtualComponentCompoundMultibodyDynamicsAnalysis
    from ._5648 import WormGearCompoundMultibodyDynamicsAnalysis
    from ._5649 import WormGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5650 import WormGearSetCompoundMultibodyDynamicsAnalysis
    from ._5651 import ZerolBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5652 import ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5653 import ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
else:
    import_structure = {
        "_5525": ["AbstractAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5526": ["AbstractShaftCompoundMultibodyDynamicsAnalysis"],
        "_5527": ["AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis"],
        "_5528": [
            "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5529": ["AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"],
        "_5530": ["AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5531": ["AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5532": ["AssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5533": ["BearingCompoundMultibodyDynamicsAnalysis"],
        "_5534": ["BeltConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5535": ["BeltDriveCompoundMultibodyDynamicsAnalysis"],
        "_5536": ["BevelDifferentialGearCompoundMultibodyDynamicsAnalysis"],
        "_5537": ["BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5538": ["BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5539": ["BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5540": ["BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis"],
        "_5541": ["BevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5542": ["BevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5543": ["BevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5544": ["BoltCompoundMultibodyDynamicsAnalysis"],
        "_5545": ["BoltedJointCompoundMultibodyDynamicsAnalysis"],
        "_5546": ["ClutchCompoundMultibodyDynamicsAnalysis"],
        "_5547": ["ClutchConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5548": ["ClutchHalfCompoundMultibodyDynamicsAnalysis"],
        "_5549": ["CoaxialConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5550": ["ComponentCompoundMultibodyDynamicsAnalysis"],
        "_5551": ["ConceptCouplingCompoundMultibodyDynamicsAnalysis"],
        "_5552": ["ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5553": ["ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5554": ["ConceptGearCompoundMultibodyDynamicsAnalysis"],
        "_5555": ["ConceptGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5556": ["ConceptGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5557": ["ConicalGearCompoundMultibodyDynamicsAnalysis"],
        "_5558": ["ConicalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5559": ["ConicalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5560": ["ConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5561": ["ConnectorCompoundMultibodyDynamicsAnalysis"],
        "_5562": ["CouplingCompoundMultibodyDynamicsAnalysis"],
        "_5563": ["CouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5564": ["CouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5565": ["CVTBeltConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5566": ["CVTCompoundMultibodyDynamicsAnalysis"],
        "_5567": ["CVTPulleyCompoundMultibodyDynamicsAnalysis"],
        "_5568": ["CycloidalAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5569": [
            "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5570": ["CycloidalDiscCompoundMultibodyDynamicsAnalysis"],
        "_5571": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5572": ["CylindricalGearCompoundMultibodyDynamicsAnalysis"],
        "_5573": ["CylindricalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5574": ["CylindricalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5575": ["CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5576": ["DatumCompoundMultibodyDynamicsAnalysis"],
        "_5577": ["ExternalCADModelCompoundMultibodyDynamicsAnalysis"],
        "_5578": ["FaceGearCompoundMultibodyDynamicsAnalysis"],
        "_5579": ["FaceGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5580": ["FaceGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5581": ["FEPartCompoundMultibodyDynamicsAnalysis"],
        "_5582": ["FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5583": ["GearCompoundMultibodyDynamicsAnalysis"],
        "_5584": ["GearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5585": ["GearSetCompoundMultibodyDynamicsAnalysis"],
        "_5586": ["GuideDxfModelCompoundMultibodyDynamicsAnalysis"],
        "_5587": ["HypoidGearCompoundMultibodyDynamicsAnalysis"],
        "_5588": ["HypoidGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5589": ["HypoidGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5590": ["InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5591": [
            "KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5592": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5593": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5594": [
            "KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5595": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5596": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5597": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5598": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5599": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5600": ["MassDiscCompoundMultibodyDynamicsAnalysis"],
        "_5601": ["MeasurementComponentCompoundMultibodyDynamicsAnalysis"],
        "_5602": ["MountableComponentCompoundMultibodyDynamicsAnalysis"],
        "_5603": ["OilSealCompoundMultibodyDynamicsAnalysis"],
        "_5604": ["PartCompoundMultibodyDynamicsAnalysis"],
        "_5605": ["PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis"],
        "_5606": ["PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5607": ["PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5608": ["PlanetaryConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5609": ["PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5610": ["PlanetCarrierCompoundMultibodyDynamicsAnalysis"],
        "_5611": ["PointLoadCompoundMultibodyDynamicsAnalysis"],
        "_5612": ["PowerLoadCompoundMultibodyDynamicsAnalysis"],
        "_5613": ["PulleyCompoundMultibodyDynamicsAnalysis"],
        "_5614": ["RingPinsCompoundMultibodyDynamicsAnalysis"],
        "_5615": ["RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5616": ["RollingRingAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5617": ["RollingRingCompoundMultibodyDynamicsAnalysis"],
        "_5618": ["RollingRingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5619": ["RootAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5620": ["ShaftCompoundMultibodyDynamicsAnalysis"],
        "_5621": ["ShaftHubConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5622": [
            "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5623": ["SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5624": ["SpiralBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5625": ["SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5626": ["SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5627": ["SpringDamperCompoundMultibodyDynamicsAnalysis"],
        "_5628": ["SpringDamperConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5629": ["SpringDamperHalfCompoundMultibodyDynamicsAnalysis"],
        "_5630": ["StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis"],
        "_5631": ["StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5632": ["StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5633": ["StraightBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5634": ["StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5635": ["StraightBevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5636": ["StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5637": ["StraightBevelSunGearCompoundMultibodyDynamicsAnalysis"],
        "_5638": ["SynchroniserCompoundMultibodyDynamicsAnalysis"],
        "_5639": ["SynchroniserHalfCompoundMultibodyDynamicsAnalysis"],
        "_5640": ["SynchroniserPartCompoundMultibodyDynamicsAnalysis"],
        "_5641": ["SynchroniserSleeveCompoundMultibodyDynamicsAnalysis"],
        "_5642": ["TorqueConverterCompoundMultibodyDynamicsAnalysis"],
        "_5643": ["TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5644": ["TorqueConverterPumpCompoundMultibodyDynamicsAnalysis"],
        "_5645": ["TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis"],
        "_5646": ["UnbalancedMassCompoundMultibodyDynamicsAnalysis"],
        "_5647": ["VirtualComponentCompoundMultibodyDynamicsAnalysis"],
        "_5648": ["WormGearCompoundMultibodyDynamicsAnalysis"],
        "_5649": ["WormGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5650": ["WormGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5651": ["ZerolBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5652": ["ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5653": ["ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "AssemblyCompoundMultibodyDynamicsAnalysis",
    "BearingCompoundMultibodyDynamicsAnalysis",
    "BeltConnectionCompoundMultibodyDynamicsAnalysis",
    "BeltDriveCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
    "BevelGearCompoundMultibodyDynamicsAnalysis",
    "BevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "BevelGearSetCompoundMultibodyDynamicsAnalysis",
    "BoltCompoundMultibodyDynamicsAnalysis",
    "BoltedJointCompoundMultibodyDynamicsAnalysis",
    "ClutchCompoundMultibodyDynamicsAnalysis",
    "ClutchConnectionCompoundMultibodyDynamicsAnalysis",
    "ClutchHalfCompoundMultibodyDynamicsAnalysis",
    "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
    "ComponentCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
    "ConceptGearCompoundMultibodyDynamicsAnalysis",
    "ConceptGearMeshCompoundMultibodyDynamicsAnalysis",
    "ConceptGearSetCompoundMultibodyDynamicsAnalysis",
    "ConicalGearCompoundMultibodyDynamicsAnalysis",
    "ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "ConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "ConnectionCompoundMultibodyDynamicsAnalysis",
    "ConnectorCompoundMultibodyDynamicsAnalysis",
    "CouplingCompoundMultibodyDynamicsAnalysis",
    "CouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "CouplingHalfCompoundMultibodyDynamicsAnalysis",
    "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
    "CVTCompoundMultibodyDynamicsAnalysis",
    "CVTPulleyCompoundMultibodyDynamicsAnalysis",
    "CycloidalAssemblyCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearMeshCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearSetCompoundMultibodyDynamicsAnalysis",
    "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
    "DatumCompoundMultibodyDynamicsAnalysis",
    "ExternalCADModelCompoundMultibodyDynamicsAnalysis",
    "FaceGearCompoundMultibodyDynamicsAnalysis",
    "FaceGearMeshCompoundMultibodyDynamicsAnalysis",
    "FaceGearSetCompoundMultibodyDynamicsAnalysis",
    "FEPartCompoundMultibodyDynamicsAnalysis",
    "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
    "GearCompoundMultibodyDynamicsAnalysis",
    "GearMeshCompoundMultibodyDynamicsAnalysis",
    "GearSetCompoundMultibodyDynamicsAnalysis",
    "GuideDxfModelCompoundMultibodyDynamicsAnalysis",
    "HypoidGearCompoundMultibodyDynamicsAnalysis",
    "HypoidGearMeshCompoundMultibodyDynamicsAnalysis",
    "HypoidGearSetCompoundMultibodyDynamicsAnalysis",
    "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "MassDiscCompoundMultibodyDynamicsAnalysis",
    "MeasurementComponentCompoundMultibodyDynamicsAnalysis",
    "MountableComponentCompoundMultibodyDynamicsAnalysis",
    "OilSealCompoundMultibodyDynamicsAnalysis",
    "PartCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis",
    "PlanetaryConnectionCompoundMultibodyDynamicsAnalysis",
    "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
    "PlanetCarrierCompoundMultibodyDynamicsAnalysis",
    "PointLoadCompoundMultibodyDynamicsAnalysis",
    "PowerLoadCompoundMultibodyDynamicsAnalysis",
    "PulleyCompoundMultibodyDynamicsAnalysis",
    "RingPinsCompoundMultibodyDynamicsAnalysis",
    "RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis",
    "RollingRingAssemblyCompoundMultibodyDynamicsAnalysis",
    "RollingRingCompoundMultibodyDynamicsAnalysis",
    "RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
    "RootAssemblyCompoundMultibodyDynamicsAnalysis",
    "ShaftCompoundMultibodyDynamicsAnalysis",
    "ShaftHubConnectionCompoundMultibodyDynamicsAnalysis",
    "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "SpringDamperCompoundMultibodyDynamicsAnalysis",
    "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
    "SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
    "SynchroniserCompoundMultibodyDynamicsAnalysis",
    "SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
    "SynchroniserPartCompoundMultibodyDynamicsAnalysis",
    "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterPumpCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
    "UnbalancedMassCompoundMultibodyDynamicsAnalysis",
    "VirtualComponentCompoundMultibodyDynamicsAnalysis",
    "WormGearCompoundMultibodyDynamicsAnalysis",
    "WormGearMeshCompoundMultibodyDynamicsAnalysis",
    "WormGearSetCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
)

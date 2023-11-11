"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6539 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6540 import AbstractShaftCriticalSpeedAnalysis
    from ._6541 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6542 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6543 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6544 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6545 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6546 import AssemblyCriticalSpeedAnalysis
    from ._6547 import BearingCriticalSpeedAnalysis
    from ._6548 import BeltConnectionCriticalSpeedAnalysis
    from ._6549 import BeltDriveCriticalSpeedAnalysis
    from ._6550 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6551 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6552 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6553 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6554 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6555 import BevelGearCriticalSpeedAnalysis
    from ._6556 import BevelGearMeshCriticalSpeedAnalysis
    from ._6557 import BevelGearSetCriticalSpeedAnalysis
    from ._6558 import BoltCriticalSpeedAnalysis
    from ._6559 import BoltedJointCriticalSpeedAnalysis
    from ._6560 import ClutchConnectionCriticalSpeedAnalysis
    from ._6561 import ClutchCriticalSpeedAnalysis
    from ._6562 import ClutchHalfCriticalSpeedAnalysis
    from ._6563 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6564 import ComponentCriticalSpeedAnalysis
    from ._6565 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6566 import ConceptCouplingCriticalSpeedAnalysis
    from ._6567 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6568 import ConceptGearCriticalSpeedAnalysis
    from ._6569 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6570 import ConceptGearSetCriticalSpeedAnalysis
    from ._6571 import ConicalGearCriticalSpeedAnalysis
    from ._6572 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6573 import ConicalGearSetCriticalSpeedAnalysis
    from ._6574 import ConnectionCriticalSpeedAnalysis
    from ._6575 import ConnectorCriticalSpeedAnalysis
    from ._6576 import CouplingConnectionCriticalSpeedAnalysis
    from ._6577 import CouplingCriticalSpeedAnalysis
    from ._6578 import CouplingHalfCriticalSpeedAnalysis
    from ._6579 import CriticalSpeedAnalysis
    from ._6580 import CriticalSpeedAnalysisDrawStyle
    from ._6581 import CriticalSpeedAnalysisOptions
    from ._6582 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6583 import CVTCriticalSpeedAnalysis
    from ._6584 import CVTPulleyCriticalSpeedAnalysis
    from ._6585 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6586 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6587 import CycloidalDiscCriticalSpeedAnalysis
    from ._6588 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6589 import CylindricalGearCriticalSpeedAnalysis
    from ._6590 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6591 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6592 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6593 import DatumCriticalSpeedAnalysis
    from ._6594 import ExternalCADModelCriticalSpeedAnalysis
    from ._6595 import FaceGearCriticalSpeedAnalysis
    from ._6596 import FaceGearMeshCriticalSpeedAnalysis
    from ._6597 import FaceGearSetCriticalSpeedAnalysis
    from ._6598 import FEPartCriticalSpeedAnalysis
    from ._6599 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6600 import GearCriticalSpeedAnalysis
    from ._6601 import GearMeshCriticalSpeedAnalysis
    from ._6602 import GearSetCriticalSpeedAnalysis
    from ._6603 import GuideDxfModelCriticalSpeedAnalysis
    from ._6604 import HypoidGearCriticalSpeedAnalysis
    from ._6605 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6606 import HypoidGearSetCriticalSpeedAnalysis
    from ._6607 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6608 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6609 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6610 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6611 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6612 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6613 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6614 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6615 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6616 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6617 import MassDiscCriticalSpeedAnalysis
    from ._6618 import MeasurementComponentCriticalSpeedAnalysis
    from ._6619 import MountableComponentCriticalSpeedAnalysis
    from ._6620 import OilSealCriticalSpeedAnalysis
    from ._6621 import PartCriticalSpeedAnalysis
    from ._6622 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6623 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6624 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6625 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6626 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6627 import PlanetCarrierCriticalSpeedAnalysis
    from ._6628 import PointLoadCriticalSpeedAnalysis
    from ._6629 import PowerLoadCriticalSpeedAnalysis
    from ._6630 import PulleyCriticalSpeedAnalysis
    from ._6631 import RingPinsCriticalSpeedAnalysis
    from ._6632 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6633 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6634 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6635 import RollingRingCriticalSpeedAnalysis
    from ._6636 import RootAssemblyCriticalSpeedAnalysis
    from ._6637 import ShaftCriticalSpeedAnalysis
    from ._6638 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6639 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6640 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6641 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6642 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6643 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6644 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6645 import SpringDamperCriticalSpeedAnalysis
    from ._6646 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6647 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6648 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6649 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6650 import StraightBevelGearCriticalSpeedAnalysis
    from ._6651 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6652 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6653 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6654 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6655 import SynchroniserCriticalSpeedAnalysis
    from ._6656 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6657 import SynchroniserPartCriticalSpeedAnalysis
    from ._6658 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6659 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6660 import TorqueConverterCriticalSpeedAnalysis
    from ._6661 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6662 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6663 import UnbalancedMassCriticalSpeedAnalysis
    from ._6664 import VirtualComponentCriticalSpeedAnalysis
    from ._6665 import WormGearCriticalSpeedAnalysis
    from ._6666 import WormGearMeshCriticalSpeedAnalysis
    from ._6667 import WormGearSetCriticalSpeedAnalysis
    from ._6668 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6669 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6670 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6539": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6540": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6541": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6542": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6543": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6544": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6545": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6546": ["AssemblyCriticalSpeedAnalysis"],
        "_6547": ["BearingCriticalSpeedAnalysis"],
        "_6548": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6549": ["BeltDriveCriticalSpeedAnalysis"],
        "_6550": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6551": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6552": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6553": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6554": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6555": ["BevelGearCriticalSpeedAnalysis"],
        "_6556": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6557": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6558": ["BoltCriticalSpeedAnalysis"],
        "_6559": ["BoltedJointCriticalSpeedAnalysis"],
        "_6560": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6561": ["ClutchCriticalSpeedAnalysis"],
        "_6562": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6563": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6564": ["ComponentCriticalSpeedAnalysis"],
        "_6565": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6566": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6567": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6568": ["ConceptGearCriticalSpeedAnalysis"],
        "_6569": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6570": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6571": ["ConicalGearCriticalSpeedAnalysis"],
        "_6572": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6573": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6574": ["ConnectionCriticalSpeedAnalysis"],
        "_6575": ["ConnectorCriticalSpeedAnalysis"],
        "_6576": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6577": ["CouplingCriticalSpeedAnalysis"],
        "_6578": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6579": ["CriticalSpeedAnalysis"],
        "_6580": ["CriticalSpeedAnalysisDrawStyle"],
        "_6581": ["CriticalSpeedAnalysisOptions"],
        "_6582": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6583": ["CVTCriticalSpeedAnalysis"],
        "_6584": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6585": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6586": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6587": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6588": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6589": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6590": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6591": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6592": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6593": ["DatumCriticalSpeedAnalysis"],
        "_6594": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6595": ["FaceGearCriticalSpeedAnalysis"],
        "_6596": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6597": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6598": ["FEPartCriticalSpeedAnalysis"],
        "_6599": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6600": ["GearCriticalSpeedAnalysis"],
        "_6601": ["GearMeshCriticalSpeedAnalysis"],
        "_6602": ["GearSetCriticalSpeedAnalysis"],
        "_6603": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6604": ["HypoidGearCriticalSpeedAnalysis"],
        "_6605": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6606": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6607": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6608": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6609": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6610": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6611": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6612": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6613": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6614": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6615": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6616": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6617": ["MassDiscCriticalSpeedAnalysis"],
        "_6618": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6619": ["MountableComponentCriticalSpeedAnalysis"],
        "_6620": ["OilSealCriticalSpeedAnalysis"],
        "_6621": ["PartCriticalSpeedAnalysis"],
        "_6622": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6623": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6624": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6625": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6626": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6627": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6628": ["PointLoadCriticalSpeedAnalysis"],
        "_6629": ["PowerLoadCriticalSpeedAnalysis"],
        "_6630": ["PulleyCriticalSpeedAnalysis"],
        "_6631": ["RingPinsCriticalSpeedAnalysis"],
        "_6632": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6633": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6634": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6635": ["RollingRingCriticalSpeedAnalysis"],
        "_6636": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6637": ["ShaftCriticalSpeedAnalysis"],
        "_6638": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6639": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6640": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6641": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6642": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6643": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6644": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6645": ["SpringDamperCriticalSpeedAnalysis"],
        "_6646": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6647": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6648": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6649": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6650": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6651": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6652": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6653": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6654": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6655": ["SynchroniserCriticalSpeedAnalysis"],
        "_6656": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6657": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6658": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6659": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6660": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6661": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6662": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6663": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6664": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6665": ["WormGearCriticalSpeedAnalysis"],
        "_6666": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6667": ["WormGearSetCriticalSpeedAnalysis"],
        "_6668": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6669": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6670": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)

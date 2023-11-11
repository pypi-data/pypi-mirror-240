"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6671 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6672 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6673 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6674 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6675 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6676 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6677 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6678 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6679 import BearingCompoundCriticalSpeedAnalysis
    from ._6680 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6681 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6682 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6683 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6684 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6685 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6686 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6687 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6688 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6689 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6690 import BoltCompoundCriticalSpeedAnalysis
    from ._6691 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6692 import ClutchCompoundCriticalSpeedAnalysis
    from ._6693 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6694 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6695 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6696 import ComponentCompoundCriticalSpeedAnalysis
    from ._6697 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6698 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6699 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6700 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6701 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6702 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6703 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6704 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6705 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6706 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6707 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6708 import CouplingCompoundCriticalSpeedAnalysis
    from ._6709 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6710 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6711 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6712 import CVTCompoundCriticalSpeedAnalysis
    from ._6713 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6714 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6715 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6716 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6717 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6718 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6719 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6720 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6721 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6722 import DatumCompoundCriticalSpeedAnalysis
    from ._6723 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6724 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6725 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6726 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6727 import FEPartCompoundCriticalSpeedAnalysis
    from ._6728 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6729 import GearCompoundCriticalSpeedAnalysis
    from ._6730 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6731 import GearSetCompoundCriticalSpeedAnalysis
    from ._6732 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6733 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6734 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6735 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6736 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6737 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6738 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6739 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6740 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6741 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6742 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6743 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6744 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6745 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6746 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6747 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6748 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6749 import OilSealCompoundCriticalSpeedAnalysis
    from ._6750 import PartCompoundCriticalSpeedAnalysis
    from ._6751 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6752 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6753 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6754 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6755 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6756 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6757 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6758 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6759 import PulleyCompoundCriticalSpeedAnalysis
    from ._6760 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6761 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6762 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6763 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6764 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6765 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6766 import ShaftCompoundCriticalSpeedAnalysis
    from ._6767 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6768 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6769 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6770 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6771 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6772 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6773 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6774 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6775 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6776 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6777 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6778 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6779 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6780 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6781 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6782 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6783 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6784 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6785 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6786 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6787 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6788 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6789 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6790 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6791 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6792 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6793 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6794 import WormGearCompoundCriticalSpeedAnalysis
    from ._6795 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6796 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6797 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6798 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6799 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6671": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6672": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6673": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6674": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6675": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6676": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6677": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6678": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6679": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6680": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6681": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6682": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6683": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6684": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6685": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6686": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6687": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6688": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6689": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6690": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6691": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6692": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6693": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6694": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6695": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6696": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6697": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6698": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6699": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6700": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6701": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6702": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6703": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6704": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6705": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6706": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6707": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6708": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6709": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6710": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6711": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6712": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6713": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6714": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6715": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6716": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6717": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6718": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6719": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6720": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6721": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6722": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6723": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6724": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6725": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6726": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6727": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6728": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6729": ["GearCompoundCriticalSpeedAnalysis"],
        "_6730": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6731": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6732": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6733": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6734": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6735": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6736": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6737": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6738": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6739": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6740": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6741": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6742": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6743": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6744": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6745": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6746": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6747": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6748": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6749": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6750": ["PartCompoundCriticalSpeedAnalysis"],
        "_6751": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6752": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6753": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6754": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6755": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6756": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6757": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6758": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6759": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6760": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6761": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6762": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6763": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6764": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6765": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6766": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6767": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6768": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6769": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6770": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6771": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6772": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6773": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6774": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6775": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6776": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6777": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6778": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6779": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6780": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6781": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6782": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6783": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6784": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6785": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6786": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6787": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6788": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6789": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6790": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6791": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6792": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6793": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6794": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6795": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6796": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6797": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6798": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6799": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)

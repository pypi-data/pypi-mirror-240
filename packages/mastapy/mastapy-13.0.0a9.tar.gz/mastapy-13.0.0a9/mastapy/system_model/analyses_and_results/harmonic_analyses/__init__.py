"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5674 import AbstractAssemblyHarmonicAnalysis
    from ._5675 import AbstractPeriodicExcitationDetail
    from ._5676 import AbstractShaftHarmonicAnalysis
    from ._5677 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5678 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5679 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5680 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5681 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5682 import AssemblyHarmonicAnalysis
    from ._5683 import BearingHarmonicAnalysis
    from ._5684 import BeltConnectionHarmonicAnalysis
    from ._5685 import BeltDriveHarmonicAnalysis
    from ._5686 import BevelDifferentialGearHarmonicAnalysis
    from ._5687 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5688 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5689 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5690 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5691 import BevelGearHarmonicAnalysis
    from ._5692 import BevelGearMeshHarmonicAnalysis
    from ._5693 import BevelGearSetHarmonicAnalysis
    from ._5694 import BoltedJointHarmonicAnalysis
    from ._5695 import BoltHarmonicAnalysis
    from ._5696 import ClutchConnectionHarmonicAnalysis
    from ._5697 import ClutchHalfHarmonicAnalysis
    from ._5698 import ClutchHarmonicAnalysis
    from ._5699 import CoaxialConnectionHarmonicAnalysis
    from ._5700 import ComplianceAndForceData
    from ._5701 import ComponentHarmonicAnalysis
    from ._5702 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5703 import ConceptCouplingHalfHarmonicAnalysis
    from ._5704 import ConceptCouplingHarmonicAnalysis
    from ._5705 import ConceptGearHarmonicAnalysis
    from ._5706 import ConceptGearMeshHarmonicAnalysis
    from ._5707 import ConceptGearSetHarmonicAnalysis
    from ._5708 import ConicalGearHarmonicAnalysis
    from ._5709 import ConicalGearMeshHarmonicAnalysis
    from ._5710 import ConicalGearSetHarmonicAnalysis
    from ._5711 import ConnectionHarmonicAnalysis
    from ._5712 import ConnectorHarmonicAnalysis
    from ._5713 import CouplingConnectionHarmonicAnalysis
    from ._5714 import CouplingHalfHarmonicAnalysis
    from ._5715 import CouplingHarmonicAnalysis
    from ._5716 import CVTBeltConnectionHarmonicAnalysis
    from ._5717 import CVTHarmonicAnalysis
    from ._5718 import CVTPulleyHarmonicAnalysis
    from ._5719 import CycloidalAssemblyHarmonicAnalysis
    from ._5720 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5721 import CycloidalDiscHarmonicAnalysis
    from ._5722 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5723 import CylindricalGearHarmonicAnalysis
    from ._5724 import CylindricalGearMeshHarmonicAnalysis
    from ._5725 import CylindricalGearSetHarmonicAnalysis
    from ._5726 import CylindricalPlanetGearHarmonicAnalysis
    from ._5727 import DatumHarmonicAnalysis
    from ._5728 import DynamicModelForHarmonicAnalysis
    from ._5729 import ElectricMachinePeriodicExcitationDetail
    from ._5730 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5731 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5732 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5733 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5734 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5735 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5736 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5737 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5738 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5739 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5740 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5741 import ExportOutputType
    from ._5742 import ExternalCADModelHarmonicAnalysis
    from ._5743 import FaceGearHarmonicAnalysis
    from ._5744 import FaceGearMeshHarmonicAnalysis
    from ._5745 import FaceGearSetHarmonicAnalysis
    from ._5746 import FEPartHarmonicAnalysis
    from ._5747 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5748 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5749 import GearHarmonicAnalysis
    from ._5750 import GearMeshExcitationDetail
    from ._5751 import GearMeshHarmonicAnalysis
    from ._5752 import GearMeshMisalignmentExcitationDetail
    from ._5753 import GearMeshTEExcitationDetail
    from ._5754 import GearSetHarmonicAnalysis
    from ._5755 import GeneralPeriodicExcitationDetail
    from ._5756 import GuideDxfModelHarmonicAnalysis
    from ._5757 import HarmonicAnalysis
    from ._5758 import HarmonicAnalysisDrawStyle
    from ._5759 import HarmonicAnalysisExportOptions
    from ._5760 import HarmonicAnalysisFEExportOptions
    from ._5761 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5762 import HarmonicAnalysisOptions
    from ._5763 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5764 import HarmonicAnalysisShaftExportOptions
    from ._5765 import HarmonicAnalysisTorqueInputType
    from ._5766 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5767 import HypoidGearHarmonicAnalysis
    from ._5768 import HypoidGearMeshHarmonicAnalysis
    from ._5769 import HypoidGearSetHarmonicAnalysis
    from ._5770 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5771 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5772 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5773 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5774 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5775 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5776 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5777 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5778 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5779 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5780 import MassDiscHarmonicAnalysis
    from ._5781 import MeasurementComponentHarmonicAnalysis
    from ._5782 import MountableComponentHarmonicAnalysis
    from ._5783 import OilSealHarmonicAnalysis
    from ._5784 import PartHarmonicAnalysis
    from ._5785 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5786 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5787 import PartToPartShearCouplingHarmonicAnalysis
    from ._5788 import PeriodicExcitationWithReferenceShaft
    from ._5789 import PlanetaryConnectionHarmonicAnalysis
    from ._5790 import PlanetaryGearSetHarmonicAnalysis
    from ._5791 import PlanetCarrierHarmonicAnalysis
    from ._5792 import PointLoadHarmonicAnalysis
    from ._5793 import PowerLoadHarmonicAnalysis
    from ._5794 import PulleyHarmonicAnalysis
    from ._5795 import ResponseCacheLevel
    from ._5796 import RingPinsHarmonicAnalysis
    from ._5797 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5798 import RollingRingAssemblyHarmonicAnalysis
    from ._5799 import RollingRingConnectionHarmonicAnalysis
    from ._5800 import RollingRingHarmonicAnalysis
    from ._5801 import RootAssemblyHarmonicAnalysis
    from ._5802 import ShaftHarmonicAnalysis
    from ._5803 import ShaftHubConnectionHarmonicAnalysis
    from ._5804 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5805 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5806 import SpecialisedAssemblyHarmonicAnalysis
    from ._5807 import SpeedOptionsForHarmonicAnalysisResults
    from ._5808 import SpiralBevelGearHarmonicAnalysis
    from ._5809 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5810 import SpiralBevelGearSetHarmonicAnalysis
    from ._5811 import SpringDamperConnectionHarmonicAnalysis
    from ._5812 import SpringDamperHalfHarmonicAnalysis
    from ._5813 import SpringDamperHarmonicAnalysis
    from ._5814 import StiffnessOptionsForHarmonicAnalysis
    from ._5815 import StraightBevelDiffGearHarmonicAnalysis
    from ._5816 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5817 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5818 import StraightBevelGearHarmonicAnalysis
    from ._5819 import StraightBevelGearMeshHarmonicAnalysis
    from ._5820 import StraightBevelGearSetHarmonicAnalysis
    from ._5821 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5822 import StraightBevelSunGearHarmonicAnalysis
    from ._5823 import SynchroniserHalfHarmonicAnalysis
    from ._5824 import SynchroniserHarmonicAnalysis
    from ._5825 import SynchroniserPartHarmonicAnalysis
    from ._5826 import SynchroniserSleeveHarmonicAnalysis
    from ._5827 import TorqueConverterConnectionHarmonicAnalysis
    from ._5828 import TorqueConverterHarmonicAnalysis
    from ._5829 import TorqueConverterPumpHarmonicAnalysis
    from ._5830 import TorqueConverterTurbineHarmonicAnalysis
    from ._5831 import UnbalancedMassExcitationDetail
    from ._5832 import UnbalancedMassHarmonicAnalysis
    from ._5833 import VirtualComponentHarmonicAnalysis
    from ._5834 import WormGearHarmonicAnalysis
    from ._5835 import WormGearMeshHarmonicAnalysis
    from ._5836 import WormGearSetHarmonicAnalysis
    from ._5837 import ZerolBevelGearHarmonicAnalysis
    from ._5838 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5839 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5674": ["AbstractAssemblyHarmonicAnalysis"],
        "_5675": ["AbstractPeriodicExcitationDetail"],
        "_5676": ["AbstractShaftHarmonicAnalysis"],
        "_5677": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5678": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5679": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5680": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5681": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5682": ["AssemblyHarmonicAnalysis"],
        "_5683": ["BearingHarmonicAnalysis"],
        "_5684": ["BeltConnectionHarmonicAnalysis"],
        "_5685": ["BeltDriveHarmonicAnalysis"],
        "_5686": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5687": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5688": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5689": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5690": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5691": ["BevelGearHarmonicAnalysis"],
        "_5692": ["BevelGearMeshHarmonicAnalysis"],
        "_5693": ["BevelGearSetHarmonicAnalysis"],
        "_5694": ["BoltedJointHarmonicAnalysis"],
        "_5695": ["BoltHarmonicAnalysis"],
        "_5696": ["ClutchConnectionHarmonicAnalysis"],
        "_5697": ["ClutchHalfHarmonicAnalysis"],
        "_5698": ["ClutchHarmonicAnalysis"],
        "_5699": ["CoaxialConnectionHarmonicAnalysis"],
        "_5700": ["ComplianceAndForceData"],
        "_5701": ["ComponentHarmonicAnalysis"],
        "_5702": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5703": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5704": ["ConceptCouplingHarmonicAnalysis"],
        "_5705": ["ConceptGearHarmonicAnalysis"],
        "_5706": ["ConceptGearMeshHarmonicAnalysis"],
        "_5707": ["ConceptGearSetHarmonicAnalysis"],
        "_5708": ["ConicalGearHarmonicAnalysis"],
        "_5709": ["ConicalGearMeshHarmonicAnalysis"],
        "_5710": ["ConicalGearSetHarmonicAnalysis"],
        "_5711": ["ConnectionHarmonicAnalysis"],
        "_5712": ["ConnectorHarmonicAnalysis"],
        "_5713": ["CouplingConnectionHarmonicAnalysis"],
        "_5714": ["CouplingHalfHarmonicAnalysis"],
        "_5715": ["CouplingHarmonicAnalysis"],
        "_5716": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5717": ["CVTHarmonicAnalysis"],
        "_5718": ["CVTPulleyHarmonicAnalysis"],
        "_5719": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5720": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5721": ["CycloidalDiscHarmonicAnalysis"],
        "_5722": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5723": ["CylindricalGearHarmonicAnalysis"],
        "_5724": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5725": ["CylindricalGearSetHarmonicAnalysis"],
        "_5726": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5727": ["DatumHarmonicAnalysis"],
        "_5728": ["DynamicModelForHarmonicAnalysis"],
        "_5729": ["ElectricMachinePeriodicExcitationDetail"],
        "_5730": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5731": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5732": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5733": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5734": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5735": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5736": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5737": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5738": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5739": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5740": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5741": ["ExportOutputType"],
        "_5742": ["ExternalCADModelHarmonicAnalysis"],
        "_5743": ["FaceGearHarmonicAnalysis"],
        "_5744": ["FaceGearMeshHarmonicAnalysis"],
        "_5745": ["FaceGearSetHarmonicAnalysis"],
        "_5746": ["FEPartHarmonicAnalysis"],
        "_5747": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5748": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5749": ["GearHarmonicAnalysis"],
        "_5750": ["GearMeshExcitationDetail"],
        "_5751": ["GearMeshHarmonicAnalysis"],
        "_5752": ["GearMeshMisalignmentExcitationDetail"],
        "_5753": ["GearMeshTEExcitationDetail"],
        "_5754": ["GearSetHarmonicAnalysis"],
        "_5755": ["GeneralPeriodicExcitationDetail"],
        "_5756": ["GuideDxfModelHarmonicAnalysis"],
        "_5757": ["HarmonicAnalysis"],
        "_5758": ["HarmonicAnalysisDrawStyle"],
        "_5759": ["HarmonicAnalysisExportOptions"],
        "_5760": ["HarmonicAnalysisFEExportOptions"],
        "_5761": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5762": ["HarmonicAnalysisOptions"],
        "_5763": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5764": ["HarmonicAnalysisShaftExportOptions"],
        "_5765": ["HarmonicAnalysisTorqueInputType"],
        "_5766": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5767": ["HypoidGearHarmonicAnalysis"],
        "_5768": ["HypoidGearMeshHarmonicAnalysis"],
        "_5769": ["HypoidGearSetHarmonicAnalysis"],
        "_5770": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5771": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5772": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5773": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5774": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5775": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5776": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5777": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5778": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5779": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5780": ["MassDiscHarmonicAnalysis"],
        "_5781": ["MeasurementComponentHarmonicAnalysis"],
        "_5782": ["MountableComponentHarmonicAnalysis"],
        "_5783": ["OilSealHarmonicAnalysis"],
        "_5784": ["PartHarmonicAnalysis"],
        "_5785": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5786": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5787": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5788": ["PeriodicExcitationWithReferenceShaft"],
        "_5789": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5790": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5791": ["PlanetCarrierHarmonicAnalysis"],
        "_5792": ["PointLoadHarmonicAnalysis"],
        "_5793": ["PowerLoadHarmonicAnalysis"],
        "_5794": ["PulleyHarmonicAnalysis"],
        "_5795": ["ResponseCacheLevel"],
        "_5796": ["RingPinsHarmonicAnalysis"],
        "_5797": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5798": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5799": ["RollingRingConnectionHarmonicAnalysis"],
        "_5800": ["RollingRingHarmonicAnalysis"],
        "_5801": ["RootAssemblyHarmonicAnalysis"],
        "_5802": ["ShaftHarmonicAnalysis"],
        "_5803": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5804": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5805": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5806": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5807": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5808": ["SpiralBevelGearHarmonicAnalysis"],
        "_5809": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5810": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5811": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5812": ["SpringDamperHalfHarmonicAnalysis"],
        "_5813": ["SpringDamperHarmonicAnalysis"],
        "_5814": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5815": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5816": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5817": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5818": ["StraightBevelGearHarmonicAnalysis"],
        "_5819": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5820": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5821": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5822": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5823": ["SynchroniserHalfHarmonicAnalysis"],
        "_5824": ["SynchroniserHarmonicAnalysis"],
        "_5825": ["SynchroniserPartHarmonicAnalysis"],
        "_5826": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5827": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5828": ["TorqueConverterHarmonicAnalysis"],
        "_5829": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5830": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5831": ["UnbalancedMassExcitationDetail"],
        "_5832": ["UnbalancedMassHarmonicAnalysis"],
        "_5833": ["VirtualComponentHarmonicAnalysis"],
        "_5834": ["WormGearHarmonicAnalysis"],
        "_5835": ["WormGearMeshHarmonicAnalysis"],
        "_5836": ["WormGearSetHarmonicAnalysis"],
        "_5837": ["ZerolBevelGearHarmonicAnalysis"],
        "_5838": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5839": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)

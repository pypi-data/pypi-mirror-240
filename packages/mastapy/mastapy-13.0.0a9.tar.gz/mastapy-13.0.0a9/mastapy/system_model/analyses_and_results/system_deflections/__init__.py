"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2682 import AbstractAssemblySystemDeflection
    from ._2683 import AbstractShaftOrHousingSystemDeflection
    from ._2684 import AbstractShaftSystemDeflection
    from ._2685 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2686 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2687 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2688 import AGMAGleasonConicalGearSystemDeflection
    from ._2689 import AssemblySystemDeflection
    from ._2690 import BearingDynamicElementContactPropertyWrapper
    from ._2691 import BearingDynamicElementPropertyWrapper
    from ._2692 import BearingDynamicPostAnalysisResultWrapper
    from ._2693 import BearingDynamicResultsPropertyWrapper
    from ._2694 import BearingDynamicResultsUIWrapper
    from ._2695 import BearingSystemDeflection
    from ._2696 import BeltConnectionSystemDeflection
    from ._2697 import BeltDriveSystemDeflection
    from ._2698 import BevelDifferentialGearMeshSystemDeflection
    from ._2699 import BevelDifferentialGearSetSystemDeflection
    from ._2700 import BevelDifferentialGearSystemDeflection
    from ._2701 import BevelDifferentialPlanetGearSystemDeflection
    from ._2702 import BevelDifferentialSunGearSystemDeflection
    from ._2703 import BevelGearMeshSystemDeflection
    from ._2704 import BevelGearSetSystemDeflection
    from ._2705 import BevelGearSystemDeflection
    from ._2706 import BoltedJointSystemDeflection
    from ._2707 import BoltSystemDeflection
    from ._2708 import ClutchConnectionSystemDeflection
    from ._2709 import ClutchHalfSystemDeflection
    from ._2710 import ClutchSystemDeflection
    from ._2711 import CoaxialConnectionSystemDeflection
    from ._2712 import ComponentSystemDeflection
    from ._2713 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2714 import ConceptCouplingConnectionSystemDeflection
    from ._2715 import ConceptCouplingHalfSystemDeflection
    from ._2716 import ConceptCouplingSystemDeflection
    from ._2717 import ConceptGearMeshSystemDeflection
    from ._2718 import ConceptGearSetSystemDeflection
    from ._2719 import ConceptGearSystemDeflection
    from ._2720 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2721 import ConicalGearMeshSystemDeflection
    from ._2722 import ConicalGearSetSystemDeflection
    from ._2723 import ConicalGearSystemDeflection
    from ._2724 import ConnectionSystemDeflection
    from ._2725 import ConnectorSystemDeflection
    from ._2726 import CouplingConnectionSystemDeflection
    from ._2727 import CouplingHalfSystemDeflection
    from ._2728 import CouplingSystemDeflection
    from ._2729 import CVTBeltConnectionSystemDeflection
    from ._2730 import CVTPulleySystemDeflection
    from ._2731 import CVTSystemDeflection
    from ._2732 import CycloidalAssemblySystemDeflection
    from ._2733 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2734 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2735 import CycloidalDiscSystemDeflection
    from ._2736 import CylindricalGearMeshSystemDeflection
    from ._2737 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2738 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2739 import CylindricalGearSetSystemDeflection
    from ._2740 import CylindricalGearSetSystemDeflectionTimestep
    from ._2741 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2742 import CylindricalGearSystemDeflection
    from ._2743 import CylindricalGearSystemDeflectionTimestep
    from ._2744 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2745 import CylindricalMeshedGearFlankSystemDeflection
    from ._2746 import CylindricalMeshedGearSystemDeflection
    from ._2747 import CylindricalPlanetGearSystemDeflection
    from ._2748 import DatumSystemDeflection
    from ._2749 import ExternalCADModelSystemDeflection
    from ._2750 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2751 import FaceGearMeshSystemDeflection
    from ._2752 import FaceGearSetSystemDeflection
    from ._2753 import FaceGearSystemDeflection
    from ._2754 import FEPartSystemDeflection
    from ._2755 import FlexiblePinAssemblySystemDeflection
    from ._2756 import GearMeshSystemDeflection
    from ._2757 import GearSetSystemDeflection
    from ._2758 import GearSystemDeflection
    from ._2759 import GuideDxfModelSystemDeflection
    from ._2760 import HypoidGearMeshSystemDeflection
    from ._2761 import HypoidGearSetSystemDeflection
    from ._2762 import HypoidGearSystemDeflection
    from ._2763 import InformationForContactAtPointAlongFaceWidth
    from ._2764 import InterMountableComponentConnectionSystemDeflection
    from ._2765 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2766 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2767 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2768 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2769 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2770 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2771 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2772 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2773 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2774 import LoadCaseOverallEfficiencyResult
    from ._2775 import LoadSharingFactorReporter
    from ._2776 import MassDiscSystemDeflection
    from ._2777 import MeasurementComponentSystemDeflection
    from ._2778 import MeshSeparationsAtFaceWidth
    from ._2779 import MountableComponentSystemDeflection
    from ._2780 import ObservedPinStiffnessReporter
    from ._2781 import OilSealSystemDeflection
    from ._2782 import PartSystemDeflection
    from ._2783 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2784 import PartToPartShearCouplingHalfSystemDeflection
    from ._2785 import PartToPartShearCouplingSystemDeflection
    from ._2786 import PlanetaryConnectionSystemDeflection
    from ._2787 import PlanetCarrierSystemDeflection
    from ._2788 import PointLoadSystemDeflection
    from ._2789 import PowerLoadSystemDeflection
    from ._2790 import PulleySystemDeflection
    from ._2791 import RingPinsSystemDeflection
    from ._2792 import RingPinsToDiscConnectionSystemDeflection
    from ._2793 import RingPinToDiscContactReporting
    from ._2794 import RollingRingAssemblySystemDeflection
    from ._2795 import RollingRingConnectionSystemDeflection
    from ._2796 import RollingRingSystemDeflection
    from ._2797 import RootAssemblySystemDeflection
    from ._2798 import ShaftHubConnectionSystemDeflection
    from ._2799 import ShaftSectionEndResultsSystemDeflection
    from ._2800 import ShaftSectionSystemDeflection
    from ._2801 import ShaftSystemDeflection
    from ._2802 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2803 import SpecialisedAssemblySystemDeflection
    from ._2804 import SpiralBevelGearMeshSystemDeflection
    from ._2805 import SpiralBevelGearSetSystemDeflection
    from ._2806 import SpiralBevelGearSystemDeflection
    from ._2807 import SpringDamperConnectionSystemDeflection
    from ._2808 import SpringDamperHalfSystemDeflection
    from ._2809 import SpringDamperSystemDeflection
    from ._2810 import StraightBevelDiffGearMeshSystemDeflection
    from ._2811 import StraightBevelDiffGearSetSystemDeflection
    from ._2812 import StraightBevelDiffGearSystemDeflection
    from ._2813 import StraightBevelGearMeshSystemDeflection
    from ._2814 import StraightBevelGearSetSystemDeflection
    from ._2815 import StraightBevelGearSystemDeflection
    from ._2816 import StraightBevelPlanetGearSystemDeflection
    from ._2817 import StraightBevelSunGearSystemDeflection
    from ._2818 import SynchroniserHalfSystemDeflection
    from ._2819 import SynchroniserPartSystemDeflection
    from ._2820 import SynchroniserSleeveSystemDeflection
    from ._2821 import SynchroniserSystemDeflection
    from ._2822 import SystemDeflection
    from ._2823 import SystemDeflectionDrawStyle
    from ._2824 import SystemDeflectionOptions
    from ._2825 import TorqueConverterConnectionSystemDeflection
    from ._2826 import TorqueConverterPumpSystemDeflection
    from ._2827 import TorqueConverterSystemDeflection
    from ._2828 import TorqueConverterTurbineSystemDeflection
    from ._2829 import TorsionalSystemDeflection
    from ._2830 import TransmissionErrorResult
    from ._2831 import UnbalancedMassSystemDeflection
    from ._2832 import VirtualComponentSystemDeflection
    from ._2833 import WormGearMeshSystemDeflection
    from ._2834 import WormGearSetSystemDeflection
    from ._2835 import WormGearSystemDeflection
    from ._2836 import ZerolBevelGearMeshSystemDeflection
    from ._2837 import ZerolBevelGearSetSystemDeflection
    from ._2838 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2682": ["AbstractAssemblySystemDeflection"],
        "_2683": ["AbstractShaftOrHousingSystemDeflection"],
        "_2684": ["AbstractShaftSystemDeflection"],
        "_2685": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2686": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2687": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2688": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2689": ["AssemblySystemDeflection"],
        "_2690": ["BearingDynamicElementContactPropertyWrapper"],
        "_2691": ["BearingDynamicElementPropertyWrapper"],
        "_2692": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2693": ["BearingDynamicResultsPropertyWrapper"],
        "_2694": ["BearingDynamicResultsUIWrapper"],
        "_2695": ["BearingSystemDeflection"],
        "_2696": ["BeltConnectionSystemDeflection"],
        "_2697": ["BeltDriveSystemDeflection"],
        "_2698": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2699": ["BevelDifferentialGearSetSystemDeflection"],
        "_2700": ["BevelDifferentialGearSystemDeflection"],
        "_2701": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2702": ["BevelDifferentialSunGearSystemDeflection"],
        "_2703": ["BevelGearMeshSystemDeflection"],
        "_2704": ["BevelGearSetSystemDeflection"],
        "_2705": ["BevelGearSystemDeflection"],
        "_2706": ["BoltedJointSystemDeflection"],
        "_2707": ["BoltSystemDeflection"],
        "_2708": ["ClutchConnectionSystemDeflection"],
        "_2709": ["ClutchHalfSystemDeflection"],
        "_2710": ["ClutchSystemDeflection"],
        "_2711": ["CoaxialConnectionSystemDeflection"],
        "_2712": ["ComponentSystemDeflection"],
        "_2713": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2714": ["ConceptCouplingConnectionSystemDeflection"],
        "_2715": ["ConceptCouplingHalfSystemDeflection"],
        "_2716": ["ConceptCouplingSystemDeflection"],
        "_2717": ["ConceptGearMeshSystemDeflection"],
        "_2718": ["ConceptGearSetSystemDeflection"],
        "_2719": ["ConceptGearSystemDeflection"],
        "_2720": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2721": ["ConicalGearMeshSystemDeflection"],
        "_2722": ["ConicalGearSetSystemDeflection"],
        "_2723": ["ConicalGearSystemDeflection"],
        "_2724": ["ConnectionSystemDeflection"],
        "_2725": ["ConnectorSystemDeflection"],
        "_2726": ["CouplingConnectionSystemDeflection"],
        "_2727": ["CouplingHalfSystemDeflection"],
        "_2728": ["CouplingSystemDeflection"],
        "_2729": ["CVTBeltConnectionSystemDeflection"],
        "_2730": ["CVTPulleySystemDeflection"],
        "_2731": ["CVTSystemDeflection"],
        "_2732": ["CycloidalAssemblySystemDeflection"],
        "_2733": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2734": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2735": ["CycloidalDiscSystemDeflection"],
        "_2736": ["CylindricalGearMeshSystemDeflection"],
        "_2737": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2738": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2739": ["CylindricalGearSetSystemDeflection"],
        "_2740": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2741": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2742": ["CylindricalGearSystemDeflection"],
        "_2743": ["CylindricalGearSystemDeflectionTimestep"],
        "_2744": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2745": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2746": ["CylindricalMeshedGearSystemDeflection"],
        "_2747": ["CylindricalPlanetGearSystemDeflection"],
        "_2748": ["DatumSystemDeflection"],
        "_2749": ["ExternalCADModelSystemDeflection"],
        "_2750": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2751": ["FaceGearMeshSystemDeflection"],
        "_2752": ["FaceGearSetSystemDeflection"],
        "_2753": ["FaceGearSystemDeflection"],
        "_2754": ["FEPartSystemDeflection"],
        "_2755": ["FlexiblePinAssemblySystemDeflection"],
        "_2756": ["GearMeshSystemDeflection"],
        "_2757": ["GearSetSystemDeflection"],
        "_2758": ["GearSystemDeflection"],
        "_2759": ["GuideDxfModelSystemDeflection"],
        "_2760": ["HypoidGearMeshSystemDeflection"],
        "_2761": ["HypoidGearSetSystemDeflection"],
        "_2762": ["HypoidGearSystemDeflection"],
        "_2763": ["InformationForContactAtPointAlongFaceWidth"],
        "_2764": ["InterMountableComponentConnectionSystemDeflection"],
        "_2765": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2766": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2767": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2768": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2769": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2770": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2771": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2772": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2773": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2774": ["LoadCaseOverallEfficiencyResult"],
        "_2775": ["LoadSharingFactorReporter"],
        "_2776": ["MassDiscSystemDeflection"],
        "_2777": ["MeasurementComponentSystemDeflection"],
        "_2778": ["MeshSeparationsAtFaceWidth"],
        "_2779": ["MountableComponentSystemDeflection"],
        "_2780": ["ObservedPinStiffnessReporter"],
        "_2781": ["OilSealSystemDeflection"],
        "_2782": ["PartSystemDeflection"],
        "_2783": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2784": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2785": ["PartToPartShearCouplingSystemDeflection"],
        "_2786": ["PlanetaryConnectionSystemDeflection"],
        "_2787": ["PlanetCarrierSystemDeflection"],
        "_2788": ["PointLoadSystemDeflection"],
        "_2789": ["PowerLoadSystemDeflection"],
        "_2790": ["PulleySystemDeflection"],
        "_2791": ["RingPinsSystemDeflection"],
        "_2792": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2793": ["RingPinToDiscContactReporting"],
        "_2794": ["RollingRingAssemblySystemDeflection"],
        "_2795": ["RollingRingConnectionSystemDeflection"],
        "_2796": ["RollingRingSystemDeflection"],
        "_2797": ["RootAssemblySystemDeflection"],
        "_2798": ["ShaftHubConnectionSystemDeflection"],
        "_2799": ["ShaftSectionEndResultsSystemDeflection"],
        "_2800": ["ShaftSectionSystemDeflection"],
        "_2801": ["ShaftSystemDeflection"],
        "_2802": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2803": ["SpecialisedAssemblySystemDeflection"],
        "_2804": ["SpiralBevelGearMeshSystemDeflection"],
        "_2805": ["SpiralBevelGearSetSystemDeflection"],
        "_2806": ["SpiralBevelGearSystemDeflection"],
        "_2807": ["SpringDamperConnectionSystemDeflection"],
        "_2808": ["SpringDamperHalfSystemDeflection"],
        "_2809": ["SpringDamperSystemDeflection"],
        "_2810": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2811": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2812": ["StraightBevelDiffGearSystemDeflection"],
        "_2813": ["StraightBevelGearMeshSystemDeflection"],
        "_2814": ["StraightBevelGearSetSystemDeflection"],
        "_2815": ["StraightBevelGearSystemDeflection"],
        "_2816": ["StraightBevelPlanetGearSystemDeflection"],
        "_2817": ["StraightBevelSunGearSystemDeflection"],
        "_2818": ["SynchroniserHalfSystemDeflection"],
        "_2819": ["SynchroniserPartSystemDeflection"],
        "_2820": ["SynchroniserSleeveSystemDeflection"],
        "_2821": ["SynchroniserSystemDeflection"],
        "_2822": ["SystemDeflection"],
        "_2823": ["SystemDeflectionDrawStyle"],
        "_2824": ["SystemDeflectionOptions"],
        "_2825": ["TorqueConverterConnectionSystemDeflection"],
        "_2826": ["TorqueConverterPumpSystemDeflection"],
        "_2827": ["TorqueConverterSystemDeflection"],
        "_2828": ["TorqueConverterTurbineSystemDeflection"],
        "_2829": ["TorsionalSystemDeflection"],
        "_2830": ["TransmissionErrorResult"],
        "_2831": ["UnbalancedMassSystemDeflection"],
        "_2832": ["VirtualComponentSystemDeflection"],
        "_2833": ["WormGearMeshSystemDeflection"],
        "_2834": ["WormGearSetSystemDeflection"],
        "_2835": ["WormGearSystemDeflection"],
        "_2836": ["ZerolBevelGearMeshSystemDeflection"],
        "_2837": ["ZerolBevelGearSetSystemDeflection"],
        "_2838": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2848 import AbstractAssemblyCompoundSystemDeflection
    from ._2849 import AbstractShaftCompoundSystemDeflection
    from ._2850 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2851 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2852 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2853 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2854 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2855 import AssemblyCompoundSystemDeflection
    from ._2856 import BearingCompoundSystemDeflection
    from ._2857 import BeltConnectionCompoundSystemDeflection
    from ._2858 import BeltDriveCompoundSystemDeflection
    from ._2859 import BevelDifferentialGearCompoundSystemDeflection
    from ._2860 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2861 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2862 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2863 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2864 import BevelGearCompoundSystemDeflection
    from ._2865 import BevelGearMeshCompoundSystemDeflection
    from ._2866 import BevelGearSetCompoundSystemDeflection
    from ._2867 import BoltCompoundSystemDeflection
    from ._2868 import BoltedJointCompoundSystemDeflection
    from ._2869 import ClutchCompoundSystemDeflection
    from ._2870 import ClutchConnectionCompoundSystemDeflection
    from ._2871 import ClutchHalfCompoundSystemDeflection
    from ._2872 import CoaxialConnectionCompoundSystemDeflection
    from ._2873 import ComponentCompoundSystemDeflection
    from ._2874 import ConceptCouplingCompoundSystemDeflection
    from ._2875 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2876 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2877 import ConceptGearCompoundSystemDeflection
    from ._2878 import ConceptGearMeshCompoundSystemDeflection
    from ._2879 import ConceptGearSetCompoundSystemDeflection
    from ._2880 import ConicalGearCompoundSystemDeflection
    from ._2881 import ConicalGearMeshCompoundSystemDeflection
    from ._2882 import ConicalGearSetCompoundSystemDeflection
    from ._2883 import ConnectionCompoundSystemDeflection
    from ._2884 import ConnectorCompoundSystemDeflection
    from ._2885 import CouplingCompoundSystemDeflection
    from ._2886 import CouplingConnectionCompoundSystemDeflection
    from ._2887 import CouplingHalfCompoundSystemDeflection
    from ._2888 import CVTBeltConnectionCompoundSystemDeflection
    from ._2889 import CVTCompoundSystemDeflection
    from ._2890 import CVTPulleyCompoundSystemDeflection
    from ._2891 import CycloidalAssemblyCompoundSystemDeflection
    from ._2892 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2893 import CycloidalDiscCompoundSystemDeflection
    from ._2894 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2895 import CylindricalGearCompoundSystemDeflection
    from ._2896 import CylindricalGearMeshCompoundSystemDeflection
    from ._2897 import CylindricalGearSetCompoundSystemDeflection
    from ._2898 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2899 import DatumCompoundSystemDeflection
    from ._2900 import DutyCycleEfficiencyResults
    from ._2901 import ExternalCADModelCompoundSystemDeflection
    from ._2902 import FaceGearCompoundSystemDeflection
    from ._2903 import FaceGearMeshCompoundSystemDeflection
    from ._2904 import FaceGearSetCompoundSystemDeflection
    from ._2905 import FEPartCompoundSystemDeflection
    from ._2906 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2907 import GearCompoundSystemDeflection
    from ._2908 import GearMeshCompoundSystemDeflection
    from ._2909 import GearSetCompoundSystemDeflection
    from ._2910 import GuideDxfModelCompoundSystemDeflection
    from ._2911 import HypoidGearCompoundSystemDeflection
    from ._2912 import HypoidGearMeshCompoundSystemDeflection
    from ._2913 import HypoidGearSetCompoundSystemDeflection
    from ._2914 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2915 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2916 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2917 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2918 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2919 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2920 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2921 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2922 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2923 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2924 import MassDiscCompoundSystemDeflection
    from ._2925 import MeasurementComponentCompoundSystemDeflection
    from ._2926 import MountableComponentCompoundSystemDeflection
    from ._2927 import OilSealCompoundSystemDeflection
    from ._2928 import PartCompoundSystemDeflection
    from ._2929 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2930 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2931 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2932 import PlanetaryConnectionCompoundSystemDeflection
    from ._2933 import PlanetaryGearSetCompoundSystemDeflection
    from ._2934 import PlanetCarrierCompoundSystemDeflection
    from ._2935 import PointLoadCompoundSystemDeflection
    from ._2936 import PowerLoadCompoundSystemDeflection
    from ._2937 import PulleyCompoundSystemDeflection
    from ._2938 import RingPinsCompoundSystemDeflection
    from ._2939 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2940 import RollingRingAssemblyCompoundSystemDeflection
    from ._2941 import RollingRingCompoundSystemDeflection
    from ._2942 import RollingRingConnectionCompoundSystemDeflection
    from ._2943 import RootAssemblyCompoundSystemDeflection
    from ._2944 import ShaftCompoundSystemDeflection
    from ._2945 import ShaftDutyCycleSystemDeflection
    from ._2946 import ShaftHubConnectionCompoundSystemDeflection
    from ._2947 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2948 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2949 import SpiralBevelGearCompoundSystemDeflection
    from ._2950 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2951 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2952 import SpringDamperCompoundSystemDeflection
    from ._2953 import SpringDamperConnectionCompoundSystemDeflection
    from ._2954 import SpringDamperHalfCompoundSystemDeflection
    from ._2955 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2956 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2957 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2958 import StraightBevelGearCompoundSystemDeflection
    from ._2959 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2960 import StraightBevelGearSetCompoundSystemDeflection
    from ._2961 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2962 import StraightBevelSunGearCompoundSystemDeflection
    from ._2963 import SynchroniserCompoundSystemDeflection
    from ._2964 import SynchroniserHalfCompoundSystemDeflection
    from ._2965 import SynchroniserPartCompoundSystemDeflection
    from ._2966 import SynchroniserSleeveCompoundSystemDeflection
    from ._2967 import TorqueConverterCompoundSystemDeflection
    from ._2968 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2969 import TorqueConverterPumpCompoundSystemDeflection
    from ._2970 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2971 import UnbalancedMassCompoundSystemDeflection
    from ._2972 import VirtualComponentCompoundSystemDeflection
    from ._2973 import WormGearCompoundSystemDeflection
    from ._2974 import WormGearMeshCompoundSystemDeflection
    from ._2975 import WormGearSetCompoundSystemDeflection
    from ._2976 import ZerolBevelGearCompoundSystemDeflection
    from ._2977 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._2978 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2848": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2849": ["AbstractShaftCompoundSystemDeflection"],
        "_2850": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2851": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2852": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2853": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2854": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2855": ["AssemblyCompoundSystemDeflection"],
        "_2856": ["BearingCompoundSystemDeflection"],
        "_2857": ["BeltConnectionCompoundSystemDeflection"],
        "_2858": ["BeltDriveCompoundSystemDeflection"],
        "_2859": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2860": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2861": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2862": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2863": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2864": ["BevelGearCompoundSystemDeflection"],
        "_2865": ["BevelGearMeshCompoundSystemDeflection"],
        "_2866": ["BevelGearSetCompoundSystemDeflection"],
        "_2867": ["BoltCompoundSystemDeflection"],
        "_2868": ["BoltedJointCompoundSystemDeflection"],
        "_2869": ["ClutchCompoundSystemDeflection"],
        "_2870": ["ClutchConnectionCompoundSystemDeflection"],
        "_2871": ["ClutchHalfCompoundSystemDeflection"],
        "_2872": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2873": ["ComponentCompoundSystemDeflection"],
        "_2874": ["ConceptCouplingCompoundSystemDeflection"],
        "_2875": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2876": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2877": ["ConceptGearCompoundSystemDeflection"],
        "_2878": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2879": ["ConceptGearSetCompoundSystemDeflection"],
        "_2880": ["ConicalGearCompoundSystemDeflection"],
        "_2881": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2882": ["ConicalGearSetCompoundSystemDeflection"],
        "_2883": ["ConnectionCompoundSystemDeflection"],
        "_2884": ["ConnectorCompoundSystemDeflection"],
        "_2885": ["CouplingCompoundSystemDeflection"],
        "_2886": ["CouplingConnectionCompoundSystemDeflection"],
        "_2887": ["CouplingHalfCompoundSystemDeflection"],
        "_2888": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2889": ["CVTCompoundSystemDeflection"],
        "_2890": ["CVTPulleyCompoundSystemDeflection"],
        "_2891": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2892": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2893": ["CycloidalDiscCompoundSystemDeflection"],
        "_2894": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2895": ["CylindricalGearCompoundSystemDeflection"],
        "_2896": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2897": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2898": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2899": ["DatumCompoundSystemDeflection"],
        "_2900": ["DutyCycleEfficiencyResults"],
        "_2901": ["ExternalCADModelCompoundSystemDeflection"],
        "_2902": ["FaceGearCompoundSystemDeflection"],
        "_2903": ["FaceGearMeshCompoundSystemDeflection"],
        "_2904": ["FaceGearSetCompoundSystemDeflection"],
        "_2905": ["FEPartCompoundSystemDeflection"],
        "_2906": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2907": ["GearCompoundSystemDeflection"],
        "_2908": ["GearMeshCompoundSystemDeflection"],
        "_2909": ["GearSetCompoundSystemDeflection"],
        "_2910": ["GuideDxfModelCompoundSystemDeflection"],
        "_2911": ["HypoidGearCompoundSystemDeflection"],
        "_2912": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2913": ["HypoidGearSetCompoundSystemDeflection"],
        "_2914": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2915": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2916": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2917": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2918": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2919": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2920": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2921": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2922": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2923": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2924": ["MassDiscCompoundSystemDeflection"],
        "_2925": ["MeasurementComponentCompoundSystemDeflection"],
        "_2926": ["MountableComponentCompoundSystemDeflection"],
        "_2927": ["OilSealCompoundSystemDeflection"],
        "_2928": ["PartCompoundSystemDeflection"],
        "_2929": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2930": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2931": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2932": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2933": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2934": ["PlanetCarrierCompoundSystemDeflection"],
        "_2935": ["PointLoadCompoundSystemDeflection"],
        "_2936": ["PowerLoadCompoundSystemDeflection"],
        "_2937": ["PulleyCompoundSystemDeflection"],
        "_2938": ["RingPinsCompoundSystemDeflection"],
        "_2939": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2940": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2941": ["RollingRingCompoundSystemDeflection"],
        "_2942": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2943": ["RootAssemblyCompoundSystemDeflection"],
        "_2944": ["ShaftCompoundSystemDeflection"],
        "_2945": ["ShaftDutyCycleSystemDeflection"],
        "_2946": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2947": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2948": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2949": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2950": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2951": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2952": ["SpringDamperCompoundSystemDeflection"],
        "_2953": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2954": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2955": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2956": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2957": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2958": ["StraightBevelGearCompoundSystemDeflection"],
        "_2959": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2960": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2961": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2962": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2963": ["SynchroniserCompoundSystemDeflection"],
        "_2964": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2965": ["SynchroniserPartCompoundSystemDeflection"],
        "_2966": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2967": ["TorqueConverterCompoundSystemDeflection"],
        "_2968": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2969": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2970": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2971": ["UnbalancedMassCompoundSystemDeflection"],
        "_2972": ["VirtualComponentCompoundSystemDeflection"],
        "_2973": ["WormGearCompoundSystemDeflection"],
        "_2974": ["WormGearMeshCompoundSystemDeflection"],
        "_2975": ["WormGearSetCompoundSystemDeflection"],
        "_2976": ["ZerolBevelGearCompoundSystemDeflection"],
        "_2977": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_2978": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)

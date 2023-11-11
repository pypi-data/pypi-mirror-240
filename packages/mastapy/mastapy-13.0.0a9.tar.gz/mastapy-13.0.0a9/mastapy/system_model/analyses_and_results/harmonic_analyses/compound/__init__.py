"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5875 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5876 import AbstractShaftCompoundHarmonicAnalysis
    from ._5877 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5878 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5879 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5880 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5881 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5882 import AssemblyCompoundHarmonicAnalysis
    from ._5883 import BearingCompoundHarmonicAnalysis
    from ._5884 import BeltConnectionCompoundHarmonicAnalysis
    from ._5885 import BeltDriveCompoundHarmonicAnalysis
    from ._5886 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5887 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5888 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5889 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5890 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5891 import BevelGearCompoundHarmonicAnalysis
    from ._5892 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5893 import BevelGearSetCompoundHarmonicAnalysis
    from ._5894 import BoltCompoundHarmonicAnalysis
    from ._5895 import BoltedJointCompoundHarmonicAnalysis
    from ._5896 import ClutchCompoundHarmonicAnalysis
    from ._5897 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5898 import ClutchHalfCompoundHarmonicAnalysis
    from ._5899 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5900 import ComponentCompoundHarmonicAnalysis
    from ._5901 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5902 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5903 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5904 import ConceptGearCompoundHarmonicAnalysis
    from ._5905 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5906 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5907 import ConicalGearCompoundHarmonicAnalysis
    from ._5908 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5909 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5910 import ConnectionCompoundHarmonicAnalysis
    from ._5911 import ConnectorCompoundHarmonicAnalysis
    from ._5912 import CouplingCompoundHarmonicAnalysis
    from ._5913 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5914 import CouplingHalfCompoundHarmonicAnalysis
    from ._5915 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5916 import CVTCompoundHarmonicAnalysis
    from ._5917 import CVTPulleyCompoundHarmonicAnalysis
    from ._5918 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5919 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5920 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5921 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5922 import CylindricalGearCompoundHarmonicAnalysis
    from ._5923 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5924 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5925 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5926 import DatumCompoundHarmonicAnalysis
    from ._5927 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5928 import FaceGearCompoundHarmonicAnalysis
    from ._5929 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5930 import FaceGearSetCompoundHarmonicAnalysis
    from ._5931 import FEPartCompoundHarmonicAnalysis
    from ._5932 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5933 import GearCompoundHarmonicAnalysis
    from ._5934 import GearMeshCompoundHarmonicAnalysis
    from ._5935 import GearSetCompoundHarmonicAnalysis
    from ._5936 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5937 import HypoidGearCompoundHarmonicAnalysis
    from ._5938 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5939 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5940 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5941 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5942 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5943 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5944 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5945 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5946 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5947 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5948 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5949 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5950 import MassDiscCompoundHarmonicAnalysis
    from ._5951 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5952 import MountableComponentCompoundHarmonicAnalysis
    from ._5953 import OilSealCompoundHarmonicAnalysis
    from ._5954 import PartCompoundHarmonicAnalysis
    from ._5955 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5956 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5957 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5958 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5959 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5960 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5961 import PointLoadCompoundHarmonicAnalysis
    from ._5962 import PowerLoadCompoundHarmonicAnalysis
    from ._5963 import PulleyCompoundHarmonicAnalysis
    from ._5964 import RingPinsCompoundHarmonicAnalysis
    from ._5965 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5966 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5967 import RollingRingCompoundHarmonicAnalysis
    from ._5968 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5969 import RootAssemblyCompoundHarmonicAnalysis
    from ._5970 import ShaftCompoundHarmonicAnalysis
    from ._5971 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5972 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5973 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5974 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5975 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5976 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5977 import SpringDamperCompoundHarmonicAnalysis
    from ._5978 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5979 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5980 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5981 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5982 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5983 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5984 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5985 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5986 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5987 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._5988 import SynchroniserCompoundHarmonicAnalysis
    from ._5989 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._5990 import SynchroniserPartCompoundHarmonicAnalysis
    from ._5991 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._5992 import TorqueConverterCompoundHarmonicAnalysis
    from ._5993 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._5994 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._5995 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._5996 import UnbalancedMassCompoundHarmonicAnalysis
    from ._5997 import VirtualComponentCompoundHarmonicAnalysis
    from ._5998 import WormGearCompoundHarmonicAnalysis
    from ._5999 import WormGearMeshCompoundHarmonicAnalysis
    from ._6000 import WormGearSetCompoundHarmonicAnalysis
    from ._6001 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6002 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6003 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5875": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5876": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5877": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5878": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5879": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5880": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5881": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5882": ["AssemblyCompoundHarmonicAnalysis"],
        "_5883": ["BearingCompoundHarmonicAnalysis"],
        "_5884": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5885": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5886": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5887": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5888": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5889": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5890": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5891": ["BevelGearCompoundHarmonicAnalysis"],
        "_5892": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5893": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5894": ["BoltCompoundHarmonicAnalysis"],
        "_5895": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5896": ["ClutchCompoundHarmonicAnalysis"],
        "_5897": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5898": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5899": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5900": ["ComponentCompoundHarmonicAnalysis"],
        "_5901": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5902": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5903": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5904": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5905": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5906": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5907": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5908": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5909": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5910": ["ConnectionCompoundHarmonicAnalysis"],
        "_5911": ["ConnectorCompoundHarmonicAnalysis"],
        "_5912": ["CouplingCompoundHarmonicAnalysis"],
        "_5913": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5914": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5915": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5916": ["CVTCompoundHarmonicAnalysis"],
        "_5917": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5918": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5919": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5920": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5921": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5922": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5923": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5924": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5925": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5926": ["DatumCompoundHarmonicAnalysis"],
        "_5927": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5928": ["FaceGearCompoundHarmonicAnalysis"],
        "_5929": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5930": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5931": ["FEPartCompoundHarmonicAnalysis"],
        "_5932": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5933": ["GearCompoundHarmonicAnalysis"],
        "_5934": ["GearMeshCompoundHarmonicAnalysis"],
        "_5935": ["GearSetCompoundHarmonicAnalysis"],
        "_5936": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5937": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5938": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5939": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5940": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5941": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5942": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5943": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5944": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5945": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5946": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5947": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5948": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5949": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5950": ["MassDiscCompoundHarmonicAnalysis"],
        "_5951": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5952": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5953": ["OilSealCompoundHarmonicAnalysis"],
        "_5954": ["PartCompoundHarmonicAnalysis"],
        "_5955": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5956": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5957": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5958": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5959": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5960": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5961": ["PointLoadCompoundHarmonicAnalysis"],
        "_5962": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5963": ["PulleyCompoundHarmonicAnalysis"],
        "_5964": ["RingPinsCompoundHarmonicAnalysis"],
        "_5965": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5966": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5967": ["RollingRingCompoundHarmonicAnalysis"],
        "_5968": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5969": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5970": ["ShaftCompoundHarmonicAnalysis"],
        "_5971": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5972": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5973": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5974": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_5975": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_5976": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5977": ["SpringDamperCompoundHarmonicAnalysis"],
        "_5978": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_5979": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_5980": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_5981": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_5982": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_5983": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_5984": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_5985": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_5986": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_5987": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_5988": ["SynchroniserCompoundHarmonicAnalysis"],
        "_5989": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_5990": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_5991": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_5992": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_5993": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_5994": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_5995": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_5996": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_5997": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_5998": ["WormGearCompoundHarmonicAnalysis"],
        "_5999": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6000": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6001": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6002": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6003": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)

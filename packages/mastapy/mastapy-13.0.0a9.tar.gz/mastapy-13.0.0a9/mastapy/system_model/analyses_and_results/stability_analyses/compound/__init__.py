"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3894 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3895 import AbstractShaftCompoundStabilityAnalysis
    from ._3896 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3897 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3898 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3899 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3900 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3901 import AssemblyCompoundStabilityAnalysis
    from ._3902 import BearingCompoundStabilityAnalysis
    from ._3903 import BeltConnectionCompoundStabilityAnalysis
    from ._3904 import BeltDriveCompoundStabilityAnalysis
    from ._3905 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3906 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3907 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3908 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3909 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3910 import BevelGearCompoundStabilityAnalysis
    from ._3911 import BevelGearMeshCompoundStabilityAnalysis
    from ._3912 import BevelGearSetCompoundStabilityAnalysis
    from ._3913 import BoltCompoundStabilityAnalysis
    from ._3914 import BoltedJointCompoundStabilityAnalysis
    from ._3915 import ClutchCompoundStabilityAnalysis
    from ._3916 import ClutchConnectionCompoundStabilityAnalysis
    from ._3917 import ClutchHalfCompoundStabilityAnalysis
    from ._3918 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3919 import ComponentCompoundStabilityAnalysis
    from ._3920 import ConceptCouplingCompoundStabilityAnalysis
    from ._3921 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3922 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3923 import ConceptGearCompoundStabilityAnalysis
    from ._3924 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3925 import ConceptGearSetCompoundStabilityAnalysis
    from ._3926 import ConicalGearCompoundStabilityAnalysis
    from ._3927 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3928 import ConicalGearSetCompoundStabilityAnalysis
    from ._3929 import ConnectionCompoundStabilityAnalysis
    from ._3930 import ConnectorCompoundStabilityAnalysis
    from ._3931 import CouplingCompoundStabilityAnalysis
    from ._3932 import CouplingConnectionCompoundStabilityAnalysis
    from ._3933 import CouplingHalfCompoundStabilityAnalysis
    from ._3934 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3935 import CVTCompoundStabilityAnalysis
    from ._3936 import CVTPulleyCompoundStabilityAnalysis
    from ._3937 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3938 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3939 import CycloidalDiscCompoundStabilityAnalysis
    from ._3940 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3941 import CylindricalGearCompoundStabilityAnalysis
    from ._3942 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3943 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3944 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3945 import DatumCompoundStabilityAnalysis
    from ._3946 import ExternalCADModelCompoundStabilityAnalysis
    from ._3947 import FaceGearCompoundStabilityAnalysis
    from ._3948 import FaceGearMeshCompoundStabilityAnalysis
    from ._3949 import FaceGearSetCompoundStabilityAnalysis
    from ._3950 import FEPartCompoundStabilityAnalysis
    from ._3951 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3952 import GearCompoundStabilityAnalysis
    from ._3953 import GearMeshCompoundStabilityAnalysis
    from ._3954 import GearSetCompoundStabilityAnalysis
    from ._3955 import GuideDxfModelCompoundStabilityAnalysis
    from ._3956 import HypoidGearCompoundStabilityAnalysis
    from ._3957 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3958 import HypoidGearSetCompoundStabilityAnalysis
    from ._3959 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3960 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3961 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3962 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3963 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3964 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3965 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3966 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3967 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3968 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3969 import MassDiscCompoundStabilityAnalysis
    from ._3970 import MeasurementComponentCompoundStabilityAnalysis
    from ._3971 import MountableComponentCompoundStabilityAnalysis
    from ._3972 import OilSealCompoundStabilityAnalysis
    from ._3973 import PartCompoundStabilityAnalysis
    from ._3974 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3975 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._3976 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._3977 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._3978 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._3979 import PlanetCarrierCompoundStabilityAnalysis
    from ._3980 import PointLoadCompoundStabilityAnalysis
    from ._3981 import PowerLoadCompoundStabilityAnalysis
    from ._3982 import PulleyCompoundStabilityAnalysis
    from ._3983 import RingPinsCompoundStabilityAnalysis
    from ._3984 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._3985 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._3986 import RollingRingCompoundStabilityAnalysis
    from ._3987 import RollingRingConnectionCompoundStabilityAnalysis
    from ._3988 import RootAssemblyCompoundStabilityAnalysis
    from ._3989 import ShaftCompoundStabilityAnalysis
    from ._3990 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._3991 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._3992 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._3993 import SpiralBevelGearCompoundStabilityAnalysis
    from ._3994 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._3995 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._3996 import SpringDamperCompoundStabilityAnalysis
    from ._3997 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._3998 import SpringDamperHalfCompoundStabilityAnalysis
    from ._3999 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4000 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4001 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4002 import StraightBevelGearCompoundStabilityAnalysis
    from ._4003 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4004 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4005 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4006 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4007 import SynchroniserCompoundStabilityAnalysis
    from ._4008 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4009 import SynchroniserPartCompoundStabilityAnalysis
    from ._4010 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4011 import TorqueConverterCompoundStabilityAnalysis
    from ._4012 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4013 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4014 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4015 import UnbalancedMassCompoundStabilityAnalysis
    from ._4016 import VirtualComponentCompoundStabilityAnalysis
    from ._4017 import WormGearCompoundStabilityAnalysis
    from ._4018 import WormGearMeshCompoundStabilityAnalysis
    from ._4019 import WormGearSetCompoundStabilityAnalysis
    from ._4020 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4021 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4022 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3894": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3895": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3896": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3897": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3898": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3899": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3900": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3901": ["AssemblyCompoundStabilityAnalysis"],
        "_3902": ["BearingCompoundStabilityAnalysis"],
        "_3903": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3904": ["BeltDriveCompoundStabilityAnalysis"],
        "_3905": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3906": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3907": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3908": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3909": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3910": ["BevelGearCompoundStabilityAnalysis"],
        "_3911": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3912": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3913": ["BoltCompoundStabilityAnalysis"],
        "_3914": ["BoltedJointCompoundStabilityAnalysis"],
        "_3915": ["ClutchCompoundStabilityAnalysis"],
        "_3916": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3917": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3918": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3919": ["ComponentCompoundStabilityAnalysis"],
        "_3920": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3921": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3922": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3923": ["ConceptGearCompoundStabilityAnalysis"],
        "_3924": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3925": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3926": ["ConicalGearCompoundStabilityAnalysis"],
        "_3927": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3928": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3929": ["ConnectionCompoundStabilityAnalysis"],
        "_3930": ["ConnectorCompoundStabilityAnalysis"],
        "_3931": ["CouplingCompoundStabilityAnalysis"],
        "_3932": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3933": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3934": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3935": ["CVTCompoundStabilityAnalysis"],
        "_3936": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3937": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3938": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3939": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3940": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3941": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3942": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3943": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3944": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3945": ["DatumCompoundStabilityAnalysis"],
        "_3946": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3947": ["FaceGearCompoundStabilityAnalysis"],
        "_3948": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3949": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3950": ["FEPartCompoundStabilityAnalysis"],
        "_3951": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3952": ["GearCompoundStabilityAnalysis"],
        "_3953": ["GearMeshCompoundStabilityAnalysis"],
        "_3954": ["GearSetCompoundStabilityAnalysis"],
        "_3955": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3956": ["HypoidGearCompoundStabilityAnalysis"],
        "_3957": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3958": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3959": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3960": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3961": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3962": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3963": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3964": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3965": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3966": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3967": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3968": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3969": ["MassDiscCompoundStabilityAnalysis"],
        "_3970": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3971": ["MountableComponentCompoundStabilityAnalysis"],
        "_3972": ["OilSealCompoundStabilityAnalysis"],
        "_3973": ["PartCompoundStabilityAnalysis"],
        "_3974": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_3975": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_3976": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_3977": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_3978": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_3979": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_3980": ["PointLoadCompoundStabilityAnalysis"],
        "_3981": ["PowerLoadCompoundStabilityAnalysis"],
        "_3982": ["PulleyCompoundStabilityAnalysis"],
        "_3983": ["RingPinsCompoundStabilityAnalysis"],
        "_3984": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_3985": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_3986": ["RollingRingCompoundStabilityAnalysis"],
        "_3987": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_3988": ["RootAssemblyCompoundStabilityAnalysis"],
        "_3989": ["ShaftCompoundStabilityAnalysis"],
        "_3990": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_3991": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3992": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_3993": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_3994": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_3995": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_3996": ["SpringDamperCompoundStabilityAnalysis"],
        "_3997": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_3998": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_3999": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4000": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4001": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4002": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4003": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4004": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4005": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4006": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4007": ["SynchroniserCompoundStabilityAnalysis"],
        "_4008": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4009": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4010": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4011": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4012": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4013": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4014": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4015": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4016": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4017": ["WormGearCompoundStabilityAnalysis"],
        "_4018": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4019": ["WormGearSetCompoundStabilityAnalysis"],
        "_4020": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4021": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4022": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)

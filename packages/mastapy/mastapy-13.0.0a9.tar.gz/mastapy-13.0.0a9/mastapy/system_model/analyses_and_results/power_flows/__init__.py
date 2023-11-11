"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4029 import AbstractAssemblyPowerFlow
    from ._4030 import AbstractShaftOrHousingPowerFlow
    from ._4031 import AbstractShaftPowerFlow
    from ._4032 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4033 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4034 import AGMAGleasonConicalGearPowerFlow
    from ._4035 import AGMAGleasonConicalGearSetPowerFlow
    from ._4036 import AssemblyPowerFlow
    from ._4037 import BearingPowerFlow
    from ._4038 import BeltConnectionPowerFlow
    from ._4039 import BeltDrivePowerFlow
    from ._4040 import BevelDifferentialGearMeshPowerFlow
    from ._4041 import BevelDifferentialGearPowerFlow
    from ._4042 import BevelDifferentialGearSetPowerFlow
    from ._4043 import BevelDifferentialPlanetGearPowerFlow
    from ._4044 import BevelDifferentialSunGearPowerFlow
    from ._4045 import BevelGearMeshPowerFlow
    from ._4046 import BevelGearPowerFlow
    from ._4047 import BevelGearSetPowerFlow
    from ._4048 import BoltedJointPowerFlow
    from ._4049 import BoltPowerFlow
    from ._4050 import ClutchConnectionPowerFlow
    from ._4051 import ClutchHalfPowerFlow
    from ._4052 import ClutchPowerFlow
    from ._4053 import CoaxialConnectionPowerFlow
    from ._4054 import ComponentPowerFlow
    from ._4055 import ConceptCouplingConnectionPowerFlow
    from ._4056 import ConceptCouplingHalfPowerFlow
    from ._4057 import ConceptCouplingPowerFlow
    from ._4058 import ConceptGearMeshPowerFlow
    from ._4059 import ConceptGearPowerFlow
    from ._4060 import ConceptGearSetPowerFlow
    from ._4061 import ConicalGearMeshPowerFlow
    from ._4062 import ConicalGearPowerFlow
    from ._4063 import ConicalGearSetPowerFlow
    from ._4064 import ConnectionPowerFlow
    from ._4065 import ConnectorPowerFlow
    from ._4066 import CouplingConnectionPowerFlow
    from ._4067 import CouplingHalfPowerFlow
    from ._4068 import CouplingPowerFlow
    from ._4069 import CVTBeltConnectionPowerFlow
    from ._4070 import CVTPowerFlow
    from ._4071 import CVTPulleyPowerFlow
    from ._4072 import CycloidalAssemblyPowerFlow
    from ._4073 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4074 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4075 import CycloidalDiscPowerFlow
    from ._4076 import CylindricalGearGeometricEntityDrawStyle
    from ._4077 import CylindricalGearMeshPowerFlow
    from ._4078 import CylindricalGearPowerFlow
    from ._4079 import CylindricalGearSetPowerFlow
    from ._4080 import CylindricalPlanetGearPowerFlow
    from ._4081 import DatumPowerFlow
    from ._4082 import ExternalCADModelPowerFlow
    from ._4083 import FaceGearMeshPowerFlow
    from ._4084 import FaceGearPowerFlow
    from ._4085 import FaceGearSetPowerFlow
    from ._4086 import FastPowerFlowSolution
    from ._4087 import FEPartPowerFlow
    from ._4088 import FlexiblePinAssemblyPowerFlow
    from ._4089 import GearMeshPowerFlow
    from ._4090 import GearPowerFlow
    from ._4091 import GearSetPowerFlow
    from ._4092 import GuideDxfModelPowerFlow
    from ._4093 import HypoidGearMeshPowerFlow
    from ._4094 import HypoidGearPowerFlow
    from ._4095 import HypoidGearSetPowerFlow
    from ._4096 import InterMountableComponentConnectionPowerFlow
    from ._4097 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4098 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4099 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4100 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4101 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4102 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4103 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4104 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4105 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4106 import MassDiscPowerFlow
    from ._4107 import MeasurementComponentPowerFlow
    from ._4108 import MountableComponentPowerFlow
    from ._4109 import OilSealPowerFlow
    from ._4110 import PartPowerFlow
    from ._4111 import PartToPartShearCouplingConnectionPowerFlow
    from ._4112 import PartToPartShearCouplingHalfPowerFlow
    from ._4113 import PartToPartShearCouplingPowerFlow
    from ._4114 import PlanetaryConnectionPowerFlow
    from ._4115 import PlanetaryGearSetPowerFlow
    from ._4116 import PlanetCarrierPowerFlow
    from ._4117 import PointLoadPowerFlow
    from ._4118 import PowerFlow
    from ._4119 import PowerFlowDrawStyle
    from ._4120 import PowerLoadPowerFlow
    from ._4121 import PulleyPowerFlow
    from ._4122 import RingPinsPowerFlow
    from ._4123 import RingPinsToDiscConnectionPowerFlow
    from ._4124 import RollingRingAssemblyPowerFlow
    from ._4125 import RollingRingConnectionPowerFlow
    from ._4126 import RollingRingPowerFlow
    from ._4127 import RootAssemblyPowerFlow
    from ._4128 import ShaftHubConnectionPowerFlow
    from ._4129 import ShaftPowerFlow
    from ._4130 import ShaftToMountableComponentConnectionPowerFlow
    from ._4131 import SpecialisedAssemblyPowerFlow
    from ._4132 import SpiralBevelGearMeshPowerFlow
    from ._4133 import SpiralBevelGearPowerFlow
    from ._4134 import SpiralBevelGearSetPowerFlow
    from ._4135 import SpringDamperConnectionPowerFlow
    from ._4136 import SpringDamperHalfPowerFlow
    from ._4137 import SpringDamperPowerFlow
    from ._4138 import StraightBevelDiffGearMeshPowerFlow
    from ._4139 import StraightBevelDiffGearPowerFlow
    from ._4140 import StraightBevelDiffGearSetPowerFlow
    from ._4141 import StraightBevelGearMeshPowerFlow
    from ._4142 import StraightBevelGearPowerFlow
    from ._4143 import StraightBevelGearSetPowerFlow
    from ._4144 import StraightBevelPlanetGearPowerFlow
    from ._4145 import StraightBevelSunGearPowerFlow
    from ._4146 import SynchroniserHalfPowerFlow
    from ._4147 import SynchroniserPartPowerFlow
    from ._4148 import SynchroniserPowerFlow
    from ._4149 import SynchroniserSleevePowerFlow
    from ._4150 import ToothPassingHarmonic
    from ._4151 import TorqueConverterConnectionPowerFlow
    from ._4152 import TorqueConverterPowerFlow
    from ._4153 import TorqueConverterPumpPowerFlow
    from ._4154 import TorqueConverterTurbinePowerFlow
    from ._4155 import UnbalancedMassPowerFlow
    from ._4156 import VirtualComponentPowerFlow
    from ._4157 import WormGearMeshPowerFlow
    from ._4158 import WormGearPowerFlow
    from ._4159 import WormGearSetPowerFlow
    from ._4160 import ZerolBevelGearMeshPowerFlow
    from ._4161 import ZerolBevelGearPowerFlow
    from ._4162 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4029": ["AbstractAssemblyPowerFlow"],
        "_4030": ["AbstractShaftOrHousingPowerFlow"],
        "_4031": ["AbstractShaftPowerFlow"],
        "_4032": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4033": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4034": ["AGMAGleasonConicalGearPowerFlow"],
        "_4035": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4036": ["AssemblyPowerFlow"],
        "_4037": ["BearingPowerFlow"],
        "_4038": ["BeltConnectionPowerFlow"],
        "_4039": ["BeltDrivePowerFlow"],
        "_4040": ["BevelDifferentialGearMeshPowerFlow"],
        "_4041": ["BevelDifferentialGearPowerFlow"],
        "_4042": ["BevelDifferentialGearSetPowerFlow"],
        "_4043": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4044": ["BevelDifferentialSunGearPowerFlow"],
        "_4045": ["BevelGearMeshPowerFlow"],
        "_4046": ["BevelGearPowerFlow"],
        "_4047": ["BevelGearSetPowerFlow"],
        "_4048": ["BoltedJointPowerFlow"],
        "_4049": ["BoltPowerFlow"],
        "_4050": ["ClutchConnectionPowerFlow"],
        "_4051": ["ClutchHalfPowerFlow"],
        "_4052": ["ClutchPowerFlow"],
        "_4053": ["CoaxialConnectionPowerFlow"],
        "_4054": ["ComponentPowerFlow"],
        "_4055": ["ConceptCouplingConnectionPowerFlow"],
        "_4056": ["ConceptCouplingHalfPowerFlow"],
        "_4057": ["ConceptCouplingPowerFlow"],
        "_4058": ["ConceptGearMeshPowerFlow"],
        "_4059": ["ConceptGearPowerFlow"],
        "_4060": ["ConceptGearSetPowerFlow"],
        "_4061": ["ConicalGearMeshPowerFlow"],
        "_4062": ["ConicalGearPowerFlow"],
        "_4063": ["ConicalGearSetPowerFlow"],
        "_4064": ["ConnectionPowerFlow"],
        "_4065": ["ConnectorPowerFlow"],
        "_4066": ["CouplingConnectionPowerFlow"],
        "_4067": ["CouplingHalfPowerFlow"],
        "_4068": ["CouplingPowerFlow"],
        "_4069": ["CVTBeltConnectionPowerFlow"],
        "_4070": ["CVTPowerFlow"],
        "_4071": ["CVTPulleyPowerFlow"],
        "_4072": ["CycloidalAssemblyPowerFlow"],
        "_4073": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4074": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4075": ["CycloidalDiscPowerFlow"],
        "_4076": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4077": ["CylindricalGearMeshPowerFlow"],
        "_4078": ["CylindricalGearPowerFlow"],
        "_4079": ["CylindricalGearSetPowerFlow"],
        "_4080": ["CylindricalPlanetGearPowerFlow"],
        "_4081": ["DatumPowerFlow"],
        "_4082": ["ExternalCADModelPowerFlow"],
        "_4083": ["FaceGearMeshPowerFlow"],
        "_4084": ["FaceGearPowerFlow"],
        "_4085": ["FaceGearSetPowerFlow"],
        "_4086": ["FastPowerFlowSolution"],
        "_4087": ["FEPartPowerFlow"],
        "_4088": ["FlexiblePinAssemblyPowerFlow"],
        "_4089": ["GearMeshPowerFlow"],
        "_4090": ["GearPowerFlow"],
        "_4091": ["GearSetPowerFlow"],
        "_4092": ["GuideDxfModelPowerFlow"],
        "_4093": ["HypoidGearMeshPowerFlow"],
        "_4094": ["HypoidGearPowerFlow"],
        "_4095": ["HypoidGearSetPowerFlow"],
        "_4096": ["InterMountableComponentConnectionPowerFlow"],
        "_4097": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4098": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4099": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4100": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4101": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4102": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4103": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4104": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4105": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4106": ["MassDiscPowerFlow"],
        "_4107": ["MeasurementComponentPowerFlow"],
        "_4108": ["MountableComponentPowerFlow"],
        "_4109": ["OilSealPowerFlow"],
        "_4110": ["PartPowerFlow"],
        "_4111": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4112": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4113": ["PartToPartShearCouplingPowerFlow"],
        "_4114": ["PlanetaryConnectionPowerFlow"],
        "_4115": ["PlanetaryGearSetPowerFlow"],
        "_4116": ["PlanetCarrierPowerFlow"],
        "_4117": ["PointLoadPowerFlow"],
        "_4118": ["PowerFlow"],
        "_4119": ["PowerFlowDrawStyle"],
        "_4120": ["PowerLoadPowerFlow"],
        "_4121": ["PulleyPowerFlow"],
        "_4122": ["RingPinsPowerFlow"],
        "_4123": ["RingPinsToDiscConnectionPowerFlow"],
        "_4124": ["RollingRingAssemblyPowerFlow"],
        "_4125": ["RollingRingConnectionPowerFlow"],
        "_4126": ["RollingRingPowerFlow"],
        "_4127": ["RootAssemblyPowerFlow"],
        "_4128": ["ShaftHubConnectionPowerFlow"],
        "_4129": ["ShaftPowerFlow"],
        "_4130": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4131": ["SpecialisedAssemblyPowerFlow"],
        "_4132": ["SpiralBevelGearMeshPowerFlow"],
        "_4133": ["SpiralBevelGearPowerFlow"],
        "_4134": ["SpiralBevelGearSetPowerFlow"],
        "_4135": ["SpringDamperConnectionPowerFlow"],
        "_4136": ["SpringDamperHalfPowerFlow"],
        "_4137": ["SpringDamperPowerFlow"],
        "_4138": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4139": ["StraightBevelDiffGearPowerFlow"],
        "_4140": ["StraightBevelDiffGearSetPowerFlow"],
        "_4141": ["StraightBevelGearMeshPowerFlow"],
        "_4142": ["StraightBevelGearPowerFlow"],
        "_4143": ["StraightBevelGearSetPowerFlow"],
        "_4144": ["StraightBevelPlanetGearPowerFlow"],
        "_4145": ["StraightBevelSunGearPowerFlow"],
        "_4146": ["SynchroniserHalfPowerFlow"],
        "_4147": ["SynchroniserPartPowerFlow"],
        "_4148": ["SynchroniserPowerFlow"],
        "_4149": ["SynchroniserSleevePowerFlow"],
        "_4150": ["ToothPassingHarmonic"],
        "_4151": ["TorqueConverterConnectionPowerFlow"],
        "_4152": ["TorqueConverterPowerFlow"],
        "_4153": ["TorqueConverterPumpPowerFlow"],
        "_4154": ["TorqueConverterTurbinePowerFlow"],
        "_4155": ["UnbalancedMassPowerFlow"],
        "_4156": ["VirtualComponentPowerFlow"],
        "_4157": ["WormGearMeshPowerFlow"],
        "_4158": ["WormGearPowerFlow"],
        "_4159": ["WormGearSetPowerFlow"],
        "_4160": ["ZerolBevelGearMeshPowerFlow"],
        "_4161": ["ZerolBevelGearPowerFlow"],
        "_4162": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)

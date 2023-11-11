"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4163 import AbstractAssemblyCompoundPowerFlow
    from ._4164 import AbstractShaftCompoundPowerFlow
    from ._4165 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4166 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4167 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4168 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4169 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4170 import AssemblyCompoundPowerFlow
    from ._4171 import BearingCompoundPowerFlow
    from ._4172 import BeltConnectionCompoundPowerFlow
    from ._4173 import BeltDriveCompoundPowerFlow
    from ._4174 import BevelDifferentialGearCompoundPowerFlow
    from ._4175 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4176 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4177 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4178 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4179 import BevelGearCompoundPowerFlow
    from ._4180 import BevelGearMeshCompoundPowerFlow
    from ._4181 import BevelGearSetCompoundPowerFlow
    from ._4182 import BoltCompoundPowerFlow
    from ._4183 import BoltedJointCompoundPowerFlow
    from ._4184 import ClutchCompoundPowerFlow
    from ._4185 import ClutchConnectionCompoundPowerFlow
    from ._4186 import ClutchHalfCompoundPowerFlow
    from ._4187 import CoaxialConnectionCompoundPowerFlow
    from ._4188 import ComponentCompoundPowerFlow
    from ._4189 import ConceptCouplingCompoundPowerFlow
    from ._4190 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4191 import ConceptCouplingHalfCompoundPowerFlow
    from ._4192 import ConceptGearCompoundPowerFlow
    from ._4193 import ConceptGearMeshCompoundPowerFlow
    from ._4194 import ConceptGearSetCompoundPowerFlow
    from ._4195 import ConicalGearCompoundPowerFlow
    from ._4196 import ConicalGearMeshCompoundPowerFlow
    from ._4197 import ConicalGearSetCompoundPowerFlow
    from ._4198 import ConnectionCompoundPowerFlow
    from ._4199 import ConnectorCompoundPowerFlow
    from ._4200 import CouplingCompoundPowerFlow
    from ._4201 import CouplingConnectionCompoundPowerFlow
    from ._4202 import CouplingHalfCompoundPowerFlow
    from ._4203 import CVTBeltConnectionCompoundPowerFlow
    from ._4204 import CVTCompoundPowerFlow
    from ._4205 import CVTPulleyCompoundPowerFlow
    from ._4206 import CycloidalAssemblyCompoundPowerFlow
    from ._4207 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4208 import CycloidalDiscCompoundPowerFlow
    from ._4209 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4210 import CylindricalGearCompoundPowerFlow
    from ._4211 import CylindricalGearMeshCompoundPowerFlow
    from ._4212 import CylindricalGearSetCompoundPowerFlow
    from ._4213 import CylindricalPlanetGearCompoundPowerFlow
    from ._4214 import DatumCompoundPowerFlow
    from ._4215 import ExternalCADModelCompoundPowerFlow
    from ._4216 import FaceGearCompoundPowerFlow
    from ._4217 import FaceGearMeshCompoundPowerFlow
    from ._4218 import FaceGearSetCompoundPowerFlow
    from ._4219 import FEPartCompoundPowerFlow
    from ._4220 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4221 import GearCompoundPowerFlow
    from ._4222 import GearMeshCompoundPowerFlow
    from ._4223 import GearSetCompoundPowerFlow
    from ._4224 import GuideDxfModelCompoundPowerFlow
    from ._4225 import HypoidGearCompoundPowerFlow
    from ._4226 import HypoidGearMeshCompoundPowerFlow
    from ._4227 import HypoidGearSetCompoundPowerFlow
    from ._4228 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4229 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4230 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4231 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4232 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4233 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4234 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4235 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4236 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4237 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4238 import MassDiscCompoundPowerFlow
    from ._4239 import MeasurementComponentCompoundPowerFlow
    from ._4240 import MountableComponentCompoundPowerFlow
    from ._4241 import OilSealCompoundPowerFlow
    from ._4242 import PartCompoundPowerFlow
    from ._4243 import PartToPartShearCouplingCompoundPowerFlow
    from ._4244 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4245 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4246 import PlanetaryConnectionCompoundPowerFlow
    from ._4247 import PlanetaryGearSetCompoundPowerFlow
    from ._4248 import PlanetCarrierCompoundPowerFlow
    from ._4249 import PointLoadCompoundPowerFlow
    from ._4250 import PowerLoadCompoundPowerFlow
    from ._4251 import PulleyCompoundPowerFlow
    from ._4252 import RingPinsCompoundPowerFlow
    from ._4253 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4254 import RollingRingAssemblyCompoundPowerFlow
    from ._4255 import RollingRingCompoundPowerFlow
    from ._4256 import RollingRingConnectionCompoundPowerFlow
    from ._4257 import RootAssemblyCompoundPowerFlow
    from ._4258 import ShaftCompoundPowerFlow
    from ._4259 import ShaftHubConnectionCompoundPowerFlow
    from ._4260 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4261 import SpecialisedAssemblyCompoundPowerFlow
    from ._4262 import SpiralBevelGearCompoundPowerFlow
    from ._4263 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4264 import SpiralBevelGearSetCompoundPowerFlow
    from ._4265 import SpringDamperCompoundPowerFlow
    from ._4266 import SpringDamperConnectionCompoundPowerFlow
    from ._4267 import SpringDamperHalfCompoundPowerFlow
    from ._4268 import StraightBevelDiffGearCompoundPowerFlow
    from ._4269 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4270 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4271 import StraightBevelGearCompoundPowerFlow
    from ._4272 import StraightBevelGearMeshCompoundPowerFlow
    from ._4273 import StraightBevelGearSetCompoundPowerFlow
    from ._4274 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4275 import StraightBevelSunGearCompoundPowerFlow
    from ._4276 import SynchroniserCompoundPowerFlow
    from ._4277 import SynchroniserHalfCompoundPowerFlow
    from ._4278 import SynchroniserPartCompoundPowerFlow
    from ._4279 import SynchroniserSleeveCompoundPowerFlow
    from ._4280 import TorqueConverterCompoundPowerFlow
    from ._4281 import TorqueConverterConnectionCompoundPowerFlow
    from ._4282 import TorqueConverterPumpCompoundPowerFlow
    from ._4283 import TorqueConverterTurbineCompoundPowerFlow
    from ._4284 import UnbalancedMassCompoundPowerFlow
    from ._4285 import VirtualComponentCompoundPowerFlow
    from ._4286 import WormGearCompoundPowerFlow
    from ._4287 import WormGearMeshCompoundPowerFlow
    from ._4288 import WormGearSetCompoundPowerFlow
    from ._4289 import ZerolBevelGearCompoundPowerFlow
    from ._4290 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4291 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4163": ["AbstractAssemblyCompoundPowerFlow"],
        "_4164": ["AbstractShaftCompoundPowerFlow"],
        "_4165": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4166": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4167": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4168": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4169": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4170": ["AssemblyCompoundPowerFlow"],
        "_4171": ["BearingCompoundPowerFlow"],
        "_4172": ["BeltConnectionCompoundPowerFlow"],
        "_4173": ["BeltDriveCompoundPowerFlow"],
        "_4174": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4175": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4176": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4177": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4178": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4179": ["BevelGearCompoundPowerFlow"],
        "_4180": ["BevelGearMeshCompoundPowerFlow"],
        "_4181": ["BevelGearSetCompoundPowerFlow"],
        "_4182": ["BoltCompoundPowerFlow"],
        "_4183": ["BoltedJointCompoundPowerFlow"],
        "_4184": ["ClutchCompoundPowerFlow"],
        "_4185": ["ClutchConnectionCompoundPowerFlow"],
        "_4186": ["ClutchHalfCompoundPowerFlow"],
        "_4187": ["CoaxialConnectionCompoundPowerFlow"],
        "_4188": ["ComponentCompoundPowerFlow"],
        "_4189": ["ConceptCouplingCompoundPowerFlow"],
        "_4190": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4191": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4192": ["ConceptGearCompoundPowerFlow"],
        "_4193": ["ConceptGearMeshCompoundPowerFlow"],
        "_4194": ["ConceptGearSetCompoundPowerFlow"],
        "_4195": ["ConicalGearCompoundPowerFlow"],
        "_4196": ["ConicalGearMeshCompoundPowerFlow"],
        "_4197": ["ConicalGearSetCompoundPowerFlow"],
        "_4198": ["ConnectionCompoundPowerFlow"],
        "_4199": ["ConnectorCompoundPowerFlow"],
        "_4200": ["CouplingCompoundPowerFlow"],
        "_4201": ["CouplingConnectionCompoundPowerFlow"],
        "_4202": ["CouplingHalfCompoundPowerFlow"],
        "_4203": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4204": ["CVTCompoundPowerFlow"],
        "_4205": ["CVTPulleyCompoundPowerFlow"],
        "_4206": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4207": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4208": ["CycloidalDiscCompoundPowerFlow"],
        "_4209": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4210": ["CylindricalGearCompoundPowerFlow"],
        "_4211": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4212": ["CylindricalGearSetCompoundPowerFlow"],
        "_4213": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4214": ["DatumCompoundPowerFlow"],
        "_4215": ["ExternalCADModelCompoundPowerFlow"],
        "_4216": ["FaceGearCompoundPowerFlow"],
        "_4217": ["FaceGearMeshCompoundPowerFlow"],
        "_4218": ["FaceGearSetCompoundPowerFlow"],
        "_4219": ["FEPartCompoundPowerFlow"],
        "_4220": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4221": ["GearCompoundPowerFlow"],
        "_4222": ["GearMeshCompoundPowerFlow"],
        "_4223": ["GearSetCompoundPowerFlow"],
        "_4224": ["GuideDxfModelCompoundPowerFlow"],
        "_4225": ["HypoidGearCompoundPowerFlow"],
        "_4226": ["HypoidGearMeshCompoundPowerFlow"],
        "_4227": ["HypoidGearSetCompoundPowerFlow"],
        "_4228": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4229": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4230": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4231": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4232": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4233": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4234": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4235": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4236": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4237": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4238": ["MassDiscCompoundPowerFlow"],
        "_4239": ["MeasurementComponentCompoundPowerFlow"],
        "_4240": ["MountableComponentCompoundPowerFlow"],
        "_4241": ["OilSealCompoundPowerFlow"],
        "_4242": ["PartCompoundPowerFlow"],
        "_4243": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4244": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4245": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4246": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4247": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4248": ["PlanetCarrierCompoundPowerFlow"],
        "_4249": ["PointLoadCompoundPowerFlow"],
        "_4250": ["PowerLoadCompoundPowerFlow"],
        "_4251": ["PulleyCompoundPowerFlow"],
        "_4252": ["RingPinsCompoundPowerFlow"],
        "_4253": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4254": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4255": ["RollingRingCompoundPowerFlow"],
        "_4256": ["RollingRingConnectionCompoundPowerFlow"],
        "_4257": ["RootAssemblyCompoundPowerFlow"],
        "_4258": ["ShaftCompoundPowerFlow"],
        "_4259": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4260": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4261": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4262": ["SpiralBevelGearCompoundPowerFlow"],
        "_4263": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4264": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4265": ["SpringDamperCompoundPowerFlow"],
        "_4266": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4267": ["SpringDamperHalfCompoundPowerFlow"],
        "_4268": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4269": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4270": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4271": ["StraightBevelGearCompoundPowerFlow"],
        "_4272": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4273": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4274": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4275": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4276": ["SynchroniserCompoundPowerFlow"],
        "_4277": ["SynchroniserHalfCompoundPowerFlow"],
        "_4278": ["SynchroniserPartCompoundPowerFlow"],
        "_4279": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4280": ["TorqueConverterCompoundPowerFlow"],
        "_4281": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4282": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4283": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4284": ["UnbalancedMassCompoundPowerFlow"],
        "_4285": ["VirtualComponentCompoundPowerFlow"],
        "_4286": ["WormGearCompoundPowerFlow"],
        "_4287": ["WormGearMeshCompoundPowerFlow"],
        "_4288": ["WormGearSetCompoundPowerFlow"],
        "_4289": ["ZerolBevelGearCompoundPowerFlow"],
        "_4290": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4291": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)

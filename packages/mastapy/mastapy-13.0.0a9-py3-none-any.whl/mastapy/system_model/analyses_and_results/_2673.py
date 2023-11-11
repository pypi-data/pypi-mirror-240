"""CompoundPowerFlowAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2616
from mastapy._internal.cast_exception import CastException

_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_COMPOUND_POWER_FLOW_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundPowerFlowAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2347,
        _2349,
        _2345,
        _2339,
        _2341,
        _2343,
    )
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4266,
        _4281,
        _4164,
        _4163,
        _4165,
        _4171,
        _4182,
        _4183,
        _4188,
        _4199,
        _4214,
        _4215,
        _4219,
        _4220,
        _4170,
        _4224,
        _4238,
        _4239,
        _4240,
        _4241,
        _4242,
        _4248,
        _4249,
        _4250,
        _4257,
        _4261,
        _4284,
        _4285,
        _4258,
        _4192,
        _4194,
        _4216,
        _4218,
        _4167,
        _4169,
        _4174,
        _4176,
        _4177,
        _4178,
        _4179,
        _4181,
        _4195,
        _4197,
        _4210,
        _4212,
        _4213,
        _4221,
        _4223,
        _4225,
        _4227,
        _4229,
        _4231,
        _4232,
        _4234,
        _4235,
        _4237,
        _4247,
        _4262,
        _4264,
        _4268,
        _4270,
        _4271,
        _4273,
        _4274,
        _4275,
        _4286,
        _4288,
        _4289,
        _4291,
        _4206,
        _4208,
        _4252,
        _4243,
        _4245,
        _4173,
        _4184,
        _4186,
        _4189,
        _4191,
        _4200,
        _4202,
        _4204,
        _4205,
        _4251,
        _4259,
        _4255,
        _4254,
        _4265,
        _4267,
        _4276,
        _4277,
        _4278,
        _4279,
        _4280,
        _4282,
        _4283,
        _4260,
        _4203,
        _4172,
        _4187,
        _4198,
        _4228,
        _4246,
        _4256,
        _4166,
        _4175,
        _4193,
        _4217,
        _4269,
        _4180,
        _4196,
        _4168,
        _4211,
        _4226,
        _4230,
        _4233,
        _4236,
        _4263,
        _4272,
        _4287,
        _4290,
        _4222,
        _4207,
        _4209,
        _4253,
        _4244,
        _4185,
        _4190,
        _4201,
    )
    from mastapy.system_model.part_model import (
        _2432,
        _2431,
        _2433,
        _2436,
        _2439,
        _2440,
        _2441,
        _2444,
        _2445,
        _2449,
        _2450,
        _2451,
        _2430,
        _2452,
        _2459,
        _2460,
        _2461,
        _2463,
        _2465,
        _2466,
        _2468,
        _2469,
        _2471,
        _2473,
        _2474,
        _2476,
    )
    from mastapy.system_model.part_model.shaft_model import _2479
    from mastapy.system_model.part_model.gears import (
        _2518,
        _2519,
        _2525,
        _2526,
        _2510,
        _2511,
        _2512,
        _2513,
        _2514,
        _2515,
        _2516,
        _2517,
        _2520,
        _2521,
        _2522,
        _2523,
        _2524,
        _2527,
        _2529,
        _2531,
        _2532,
        _2533,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
    )
    from mastapy.system_model.part_model.cycloidal import _2565, _2566, _2567
    from mastapy.system_model.part_model.couplings import (
        _2585,
        _2586,
        _2573,
        _2575,
        _2576,
        _2578,
        _2579,
        _2580,
        _2581,
        _2583,
        _2584,
        _2587,
        _2595,
        _2593,
        _2594,
        _2597,
        _2598,
        _2599,
        _2601,
        _2602,
        _2603,
        _2604,
        _2605,
        _2607,
    )
    from mastapy.system_model.connections_and_sockets import (
        _2292,
        _2270,
        _2265,
        _2266,
        _2269,
        _2278,
        _2284,
        _2289,
        _2262,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2298,
        _2302,
        _2308,
        _2322,
        _2300,
        _2304,
        _2296,
        _2306,
        _2312,
        _2315,
        _2316,
        _2317,
        _2320,
        _2324,
        _2326,
        _2328,
        _2310,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2332,
        _2335,
        _2338,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CompoundPowerFlowAnalysis",)


Self = TypeVar("Self", bound="CompoundPowerFlowAnalysis")


class CompoundPowerFlowAnalysis(_2616.CompoundAnalysis):
    """CompoundPowerFlowAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_POWER_FLOW_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundPowerFlowAnalysis")

    class _Cast_CompoundPowerFlowAnalysis:
        """Special nested class for casting CompoundPowerFlowAnalysis to subclasses."""

        def __init__(
            self: "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis",
            parent: "CompoundPowerFlowAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis",
        ):
            return self._parent._cast(_2616.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis",
        ):
            from mastapy import _7549

            return self._parent._cast(_7549.MarshalByRefObjectPermanent)

        @property
        def compound_power_flow_analysis(
            self: "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis",
        ) -> "CompoundPowerFlowAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundPowerFlowAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2347.SpringDamperConnection"
    ) -> "Iterable[_4266.SpringDamperConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpringDamperConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: Self, design_entity: "_2349.TorqueConverterConnection"
    ) -> "Iterable[_4281.TorqueConverterConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: Self, design_entity: "_2432.AbstractShaft"
    ) -> "Iterable[_4164.AbstractShaftCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AbstractShaftCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: Self, design_entity: "_2431.AbstractAssembly"
    ) -> "Iterable[_4163.AbstractAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AbstractAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2433.AbstractShaftOrHousing"
    ) -> "Iterable[_4165.AbstractShaftOrHousingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AbstractShaftOrHousingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: Self, design_entity: "_2436.Bearing"
    ) -> "Iterable[_4171.BearingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BearingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEARING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: Self, design_entity: "_2439.Bolt"
    ) -> "Iterable[_4182.BoltCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BoltCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: Self, design_entity: "_2440.BoltedJoint"
    ) -> "Iterable[_4183.BoltedJointCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BoltedJointCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_component(
        self: Self, design_entity: "_2441.Component"
    ) -> "Iterable[_4188.ComponentCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ComponentCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connector(
        self: Self, design_entity: "_2444.Connector"
    ) -> "Iterable[_4199.ConnectorCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConnectorCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTOR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_datum(
        self: Self, design_entity: "_2445.Datum"
    ) -> "Iterable[_4214.DatumCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.DatumCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_DATUM](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: Self, design_entity: "_2449.ExternalCADModel"
    ) -> "Iterable[_4215.ExternalCADModelCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ExternalCADModelCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: Self, design_entity: "_2450.FEPart"
    ) -> "Iterable[_4219.FEPartCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.FEPartCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FE_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: Self, design_entity: "_2451.FlexiblePinAssembly"
    ) -> "Iterable[_4220.FlexiblePinAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.FlexiblePinAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: Self, design_entity: "_2430.Assembly"
    ) -> "Iterable[_4170.AssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: Self, design_entity: "_2452.GuideDxfModel"
    ) -> "Iterable[_4224.GuideDxfModelCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.GuideDxfModelCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: Self, design_entity: "_2459.MassDisc"
    ) -> "Iterable[_4238.MassDiscCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.MassDiscCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MASS_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: Self, design_entity: "_2460.MeasurementComponent"
    ) -> "Iterable[_4239.MeasurementComponentCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.MeasurementComponentCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: Self, design_entity: "_2461.MountableComponent"
    ) -> "Iterable[_4240.MountableComponentCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.MountableComponentCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: Self, design_entity: "_2463.OilSeal"
    ) -> "Iterable[_4241.OilSealCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.OilSealCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part(
        self: Self, design_entity: "_2465.Part"
    ) -> "Iterable[_4242.PartCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PartCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: Self, design_entity: "_2466.PlanetCarrier"
    ) -> "Iterable[_4248.PlanetCarrierCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PlanetCarrierCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: Self, design_entity: "_2468.PointLoad"
    ) -> "Iterable[_4249.PointLoadCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PointLoadCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: Self, design_entity: "_2469.PowerLoad"
    ) -> "Iterable[_4250.PowerLoadCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PowerLoadCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: Self, design_entity: "_2471.RootAssembly"
    ) -> "Iterable[_4257.RootAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RootAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: Self, design_entity: "_2473.SpecialisedAssembly"
    ) -> "Iterable[_4261.SpecialisedAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpecialisedAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: Self, design_entity: "_2474.UnbalancedMass"
    ) -> "Iterable[_4284.UnbalancedMassCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.UnbalancedMassCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: Self, design_entity: "_2476.VirtualComponent"
    ) -> "Iterable[_4285.VirtualComponentCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.VirtualComponentCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: Self, design_entity: "_2479.Shaft"
    ) -> "Iterable[_4258.ShaftCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: Self, design_entity: "_2518.ConceptGear"
    ) -> "Iterable[_4192.ConceptGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: Self, design_entity: "_2519.ConceptGearSet"
    ) -> "Iterable[_4194.ConceptGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: Self, design_entity: "_2525.FaceGear"
    ) -> "Iterable[_4216.FaceGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.FaceGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: Self, design_entity: "_2526.FaceGearSet"
    ) -> "Iterable[_4218.FaceGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.FaceGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2510.AGMAGleasonConicalGear"
    ) -> "Iterable[_4167.AGMAGleasonConicalGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AGMAGleasonConicalGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2511.AGMAGleasonConicalGearSet"
    ) -> "Iterable[_4169.AGMAGleasonConicalGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AGMAGleasonConicalGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: Self, design_entity: "_2512.BevelDifferentialGear"
    ) -> "Iterable[_4174.BevelDifferentialGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2513.BevelDifferentialGearSet"
    ) -> "Iterable[_4176.BevelDifferentialGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2514.BevelDifferentialPlanetGear"
    ) -> "Iterable[_4177.BevelDifferentialPlanetGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialPlanetGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2515.BevelDifferentialSunGear"
    ) -> "Iterable[_4178.BevelDifferentialSunGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialSunGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: Self, design_entity: "_2516.BevelGear"
    ) -> "Iterable[_4179.BevelGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: Self, design_entity: "_2517.BevelGearSet"
    ) -> "Iterable[_4181.BevelGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: Self, design_entity: "_2520.ConicalGear"
    ) -> "Iterable[_4195.ConicalGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConicalGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: Self, design_entity: "_2521.ConicalGearSet"
    ) -> "Iterable[_4197.ConicalGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConicalGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: Self, design_entity: "_2522.CylindricalGear"
    ) -> "Iterable[_4210.CylindricalGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: Self, design_entity: "_2523.CylindricalGearSet"
    ) -> "Iterable[_4212.CylindricalGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2524.CylindricalPlanetGear"
    ) -> "Iterable[_4213.CylindricalPlanetGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalPlanetGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear(
        self: Self, design_entity: "_2527.Gear"
    ) -> "Iterable[_4221.GearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.GearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: Self, design_entity: "_2529.GearSet"
    ) -> "Iterable[_4223.GearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.GearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: Self, design_entity: "_2531.HypoidGear"
    ) -> "Iterable[_4225.HypoidGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: Self, design_entity: "_2532.HypoidGearSet"
    ) -> "Iterable[_4227.HypoidGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2533.KlingelnbergCycloPalloidConicalGear"
    ) -> "Iterable[_4229.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2534.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "Iterable[_4231.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2535.KlingelnbergCycloPalloidHypoidGear"
    ) -> "Iterable[_4232.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2536.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "Iterable[_4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2537.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "Iterable[_4235.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2538.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "Iterable[_4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: Self, design_entity: "_2539.PlanetaryGearSet"
    ) -> "Iterable[_4247.PlanetaryGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PlanetaryGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: Self, design_entity: "_2540.SpiralBevelGear"
    ) -> "Iterable[_4262.SpiralBevelGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2541.SpiralBevelGearSet"
    ) -> "Iterable[_4264.SpiralBevelGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2542.StraightBevelDiffGear"
    ) -> "Iterable[_4268.StraightBevelDiffGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2543.StraightBevelDiffGearSet"
    ) -> "Iterable[_4270.StraightBevelDiffGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: Self, design_entity: "_2544.StraightBevelGear"
    ) -> "Iterable[_4271.StraightBevelGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2545.StraightBevelGearSet"
    ) -> "Iterable[_4273.StraightBevelGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2546.StraightBevelPlanetGear"
    ) -> "Iterable[_4274.StraightBevelPlanetGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelPlanetGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2547.StraightBevelSunGear"
    ) -> "Iterable[_4275.StraightBevelSunGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelSunGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: Self, design_entity: "_2548.WormGear"
    ) -> "Iterable[_4286.WormGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: Self, design_entity: "_2549.WormGearSet"
    ) -> "Iterable[_4288.WormGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: Self, design_entity: "_2550.ZerolBevelGear"
    ) -> "Iterable[_4289.ZerolBevelGearCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2551.ZerolBevelGearSet"
    ) -> "Iterable[_4291.ZerolBevelGearSetCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearSetCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: Self, design_entity: "_2565.CycloidalAssembly"
    ) -> "Iterable[_4206.CycloidalAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: Self, design_entity: "_2566.CycloidalDisc"
    ) -> "Iterable[_4208.CycloidalDiscCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalDiscCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: Self, design_entity: "_2567.RingPins"
    ) -> "Iterable[_4252.RingPinsCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RingPinsCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2585.PartToPartShearCoupling"
    ) -> "Iterable[_4243.PartToPartShearCouplingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PartToPartShearCouplingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2586.PartToPartShearCouplingHalf"
    ) -> "Iterable[_4245.PartToPartShearCouplingHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PartToPartShearCouplingHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: Self, design_entity: "_2573.BeltDrive"
    ) -> "Iterable[_4173.BeltDriveCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BeltDriveCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: Self, design_entity: "_2575.Clutch"
    ) -> "Iterable[_4184.ClutchCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ClutchCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: Self, design_entity: "_2576.ClutchHalf"
    ) -> "Iterable[_4186.ClutchHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ClutchHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: Self, design_entity: "_2578.ConceptCoupling"
    ) -> "Iterable[_4189.ConceptCouplingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptCouplingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: Self, design_entity: "_2579.ConceptCouplingHalf"
    ) -> "Iterable[_4191.ConceptCouplingHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptCouplingHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: Self, design_entity: "_2580.Coupling"
    ) -> "Iterable[_4200.CouplingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CouplingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: Self, design_entity: "_2581.CouplingHalf"
    ) -> "Iterable[_4202.CouplingHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CouplingHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: Self, design_entity: "_2583.CVT"
    ) -> "Iterable[_4204.CVTCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CVTCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: Self, design_entity: "_2584.CVTPulley"
    ) -> "Iterable[_4205.CVTPulleyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CVTPulleyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: Self, design_entity: "_2587.Pulley"
    ) -> "Iterable[_4251.PulleyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PulleyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: Self, design_entity: "_2595.ShaftHubConnection"
    ) -> "Iterable[_4259.ShaftHubConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftHubConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: Self, design_entity: "_2593.RollingRing"
    ) -> "Iterable[_4255.RollingRingCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RollingRingCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: Self, design_entity: "_2594.RollingRingAssembly"
    ) -> "Iterable[_4254.RollingRingAssemblyCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RollingRingAssemblyCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: Self, design_entity: "_2597.SpringDamper"
    ) -> "Iterable[_4265.SpringDamperCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpringDamperCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: Self, design_entity: "_2598.SpringDamperHalf"
    ) -> "Iterable[_4267.SpringDamperHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpringDamperHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: Self, design_entity: "_2599.Synchroniser"
    ) -> "Iterable[_4276.SynchroniserCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: Self, design_entity: "_2601.SynchroniserHalf"
    ) -> "Iterable[_4277.SynchroniserHalfCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserHalfCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: Self, design_entity: "_2602.SynchroniserPart"
    ) -> "Iterable[_4278.SynchroniserPartCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserPartCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: Self, design_entity: "_2603.SynchroniserSleeve"
    ) -> "Iterable[_4279.SynchroniserSleeveCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserSleeveCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: Self, design_entity: "_2604.TorqueConverter"
    ) -> "Iterable[_4280.TorqueConverterCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: Self, design_entity: "_2605.TorqueConverterPump"
    ) -> "Iterable[_4282.TorqueConverterPumpCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterPumpCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: Self, design_entity: "_2607.TorqueConverterTurbine"
    ) -> "Iterable[_4283.TorqueConverterTurbineCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterTurbineCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2292.ShaftToMountableComponentConnection"
    ) -> "Iterable[_4260.ShaftToMountableComponentConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftToMountableComponentConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: Self, design_entity: "_2270.CVTBeltConnection"
    ) -> "Iterable[_4203.CVTBeltConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CVTBeltConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: Self, design_entity: "_2265.BeltConnection"
    ) -> "Iterable[_4172.BeltConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BeltConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: Self, design_entity: "_2266.CoaxialConnection"
    ) -> "Iterable[_4187.CoaxialConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CoaxialConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connection(
        self: Self, design_entity: "_2269.Connection"
    ) -> "Iterable[_4198.ConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2278.InterMountableComponentConnection"
    ) -> "Iterable[_4228.InterMountableComponentConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.InterMountableComponentConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: Self, design_entity: "_2284.PlanetaryConnection"
    ) -> "Iterable[_4246.PlanetaryConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PlanetaryConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: Self, design_entity: "_2289.RollingRingConnection"
    ) -> "Iterable[_4256.RollingRingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RollingRingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2262.AbstractShaftToMountableComponentConnection"
    ) -> "Iterable[_4166.AbstractShaftToMountableComponentConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AbstractShaftToMountableComponentConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2298.BevelDifferentialGearMesh"
    ) -> "Iterable[_4175.BevelDifferentialGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: Self, design_entity: "_2302.ConceptGearMesh"
    ) -> "Iterable[_4193.ConceptGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: Self, design_entity: "_2308.FaceGearMesh"
    ) -> "Iterable[_4217.FaceGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.FaceGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2322.StraightBevelDiffGearMesh"
    ) -> "Iterable[_4269.StraightBevelDiffGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: Self, design_entity: "_2300.BevelGearMesh"
    ) -> "Iterable[_4180.BevelGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.BevelGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: Self, design_entity: "_2304.ConicalGearMesh"
    ) -> "Iterable[_4196.ConicalGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConicalGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2296.AGMAGleasonConicalGearMesh"
    ) -> "Iterable[_4168.AGMAGleasonConicalGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.AGMAGleasonConicalGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2306.CylindricalGearMesh"
    ) -> "Iterable[_4211.CylindricalGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2312.HypoidGearMesh"
    ) -> "Iterable[_4226.HypoidGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2315.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "Iterable[_4230.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2316.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "Iterable[_4233.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2317.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "Iterable[_4236.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2320.SpiralBevelGearMesh"
    ) -> "Iterable[_4263.SpiralBevelGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2324.StraightBevelGearMesh"
    ) -> "Iterable[_4272.StraightBevelGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: Self, design_entity: "_2326.WormGearMesh"
    ) -> "Iterable[_4287.WormGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2328.ZerolBevelGearMesh"
    ) -> "Iterable[_4290.ZerolBevelGearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: Self, design_entity: "_2310.GearMesh"
    ) -> "Iterable[_4222.GearMeshCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.GearMeshCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2332.CycloidalDiscCentralBearingConnection"
    ) -> "Iterable[_4207.CycloidalDiscCentralBearingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalDiscCentralBearingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2335.CycloidalDiscPlanetaryBearingConnection"
    ) -> "Iterable[_4209.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2338.RingPinsToDiscConnection"
    ) -> "Iterable[_4253.RingPinsToDiscConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.RingPinsToDiscConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2345.PartToPartShearCouplingConnection"
    ) -> "Iterable[_4244.PartToPartShearCouplingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.PartToPartShearCouplingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: Self, design_entity: "_2339.ClutchConnection"
    ) -> "Iterable[_4185.ClutchConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ClutchConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: Self, design_entity: "_2341.ConceptCouplingConnection"
    ) -> "Iterable[_4190.ConceptCouplingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptCouplingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: Self, design_entity: "_2343.CouplingConnection"
    ) -> "Iterable[_4201.CouplingConnectionCompoundPowerFlow]":
        """Iterable[mastapy.system_model.analyses_and_results.power_flows.compound.CouplingConnectionCompoundPowerFlow]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundPowerFlowAnalysis._Cast_CompoundPowerFlowAnalysis":
        return self._Cast_CompoundPowerFlowAnalysis(self)

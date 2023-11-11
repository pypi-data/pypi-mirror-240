"""CompoundSystemDeflectionAnalysis"""
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
_COMPOUND_SYSTEM_DEFLECTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundSystemDeflectionAnalysis"
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
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2953,
        _2968,
        _2849,
        _2848,
        _2850,
        _2856,
        _2867,
        _2868,
        _2873,
        _2884,
        _2899,
        _2901,
        _2905,
        _2906,
        _2855,
        _2910,
        _2924,
        _2925,
        _2926,
        _2927,
        _2928,
        _2934,
        _2935,
        _2936,
        _2943,
        _2948,
        _2971,
        _2972,
        _2944,
        _2877,
        _2879,
        _2902,
        _2904,
        _2852,
        _2854,
        _2859,
        _2861,
        _2862,
        _2863,
        _2864,
        _2866,
        _2880,
        _2882,
        _2895,
        _2897,
        _2898,
        _2907,
        _2909,
        _2911,
        _2913,
        _2915,
        _2917,
        _2918,
        _2920,
        _2921,
        _2923,
        _2933,
        _2949,
        _2951,
        _2955,
        _2957,
        _2958,
        _2960,
        _2961,
        _2962,
        _2973,
        _2975,
        _2976,
        _2978,
        _2891,
        _2893,
        _2938,
        _2929,
        _2931,
        _2858,
        _2869,
        _2871,
        _2874,
        _2876,
        _2885,
        _2887,
        _2889,
        _2890,
        _2937,
        _2946,
        _2941,
        _2940,
        _2952,
        _2954,
        _2963,
        _2964,
        _2965,
        _2966,
        _2967,
        _2969,
        _2970,
        _2947,
        _2888,
        _2857,
        _2872,
        _2883,
        _2914,
        _2932,
        _2942,
        _2851,
        _2860,
        _2878,
        _2903,
        _2956,
        _2865,
        _2881,
        _2853,
        _2896,
        _2912,
        _2916,
        _2919,
        _2922,
        _2950,
        _2959,
        _2974,
        _2977,
        _2908,
        _2892,
        _2894,
        _2939,
        _2930,
        _2870,
        _2875,
        _2886,
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
__all__ = ("CompoundSystemDeflectionAnalysis",)


Self = TypeVar("Self", bound="CompoundSystemDeflectionAnalysis")


class CompoundSystemDeflectionAnalysis(_2616.CompoundAnalysis):
    """CompoundSystemDeflectionAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_SYSTEM_DEFLECTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundSystemDeflectionAnalysis")

    class _Cast_CompoundSystemDeflectionAnalysis:
        """Special nested class for casting CompoundSystemDeflectionAnalysis to subclasses."""

        def __init__(
            self: "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
            parent: "CompoundSystemDeflectionAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
        ):
            return self._parent._cast(_2616.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
        ):
            from mastapy import _7549

            return self._parent._cast(_7549.MarshalByRefObjectPermanent)

        @property
        def compound_system_deflection_analysis(
            self: "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
        ) -> "CompoundSystemDeflectionAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundSystemDeflectionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2347.SpringDamperConnection"
    ) -> "Iterable[_2953.SpringDamperConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpringDamperConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2968.TorqueConverterConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.TorqueConverterConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2849.AbstractShaftCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AbstractShaftCompoundSystemDeflection]

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
    ) -> "Iterable[_2848.AbstractAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AbstractAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2850.AbstractShaftOrHousingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AbstractShaftOrHousingCompoundSystemDeflection]

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
    ) -> "Iterable[_2856.BearingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BearingCompoundSystemDeflection]

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
    ) -> "Iterable[_2867.BoltCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BoltCompoundSystemDeflection]

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
    ) -> "Iterable[_2868.BoltedJointCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BoltedJointCompoundSystemDeflection]

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
    ) -> "Iterable[_2873.ComponentCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ComponentCompoundSystemDeflection]

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
    ) -> "Iterable[_2884.ConnectorCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConnectorCompoundSystemDeflection]

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
    ) -> "Iterable[_2899.DatumCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.DatumCompoundSystemDeflection]

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
    ) -> "Iterable[_2901.ExternalCADModelCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ExternalCADModelCompoundSystemDeflection]

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
    ) -> "Iterable[_2905.FEPartCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.FEPartCompoundSystemDeflection]

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
    ) -> "Iterable[_2906.FlexiblePinAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.FlexiblePinAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2855.AssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2910.GuideDxfModelCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.GuideDxfModelCompoundSystemDeflection]

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
    ) -> "Iterable[_2924.MassDiscCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.MassDiscCompoundSystemDeflection]

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
    ) -> "Iterable[_2925.MeasurementComponentCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.MeasurementComponentCompoundSystemDeflection]

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
    ) -> "Iterable[_2926.MountableComponentCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.MountableComponentCompoundSystemDeflection]

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
    ) -> "Iterable[_2927.OilSealCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.OilSealCompoundSystemDeflection]

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
    ) -> "Iterable[_2928.PartCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PartCompoundSystemDeflection]

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
    ) -> "Iterable[_2934.PlanetCarrierCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PlanetCarrierCompoundSystemDeflection]

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
    ) -> "Iterable[_2935.PointLoadCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PointLoadCompoundSystemDeflection]

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
    ) -> "Iterable[_2936.PowerLoadCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PowerLoadCompoundSystemDeflection]

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
    ) -> "Iterable[_2943.RootAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RootAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2948.SpecialisedAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpecialisedAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2971.UnbalancedMassCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.UnbalancedMassCompoundSystemDeflection]

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
    ) -> "Iterable[_2972.VirtualComponentCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.VirtualComponentCompoundSystemDeflection]

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
    ) -> "Iterable[_2944.ShaftCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftCompoundSystemDeflection]

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
    ) -> "Iterable[_2877.ConceptGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2879.ConceptGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2902.FaceGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.FaceGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2904.FaceGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.FaceGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2852.AGMAGleasonConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2854.AGMAGleasonConicalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2859.BevelDifferentialGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2861.BevelDifferentialGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2862.BevelDifferentialPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialPlanetGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2863.BevelDifferentialSunGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialSunGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2864.BevelGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2866.BevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2880.ConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConicalGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2882.ConicalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConicalGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2895.CylindricalGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2897.CylindricalGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2898.CylindricalPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalPlanetGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2907.GearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.GearCompoundSystemDeflection]

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
    ) -> "Iterable[_2909.GearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.GearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2911.HypoidGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.HypoidGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2913.HypoidGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.HypoidGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2915.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection]

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
    ) -> (
        "Iterable[_2917.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2918.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection]

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
    ) -> (
        "Iterable[_2920.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2921.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2923.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2933.PlanetaryGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PlanetaryGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2949.SpiralBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2951.SpiralBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2955.StraightBevelDiffGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2957.StraightBevelDiffGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2958.StraightBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2960.StraightBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2961.StraightBevelPlanetGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelPlanetGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2962.StraightBevelSunGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelSunGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2973.WormGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.WormGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2975.WormGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.WormGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2976.ZerolBevelGearCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearCompoundSystemDeflection]

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
    ) -> "Iterable[_2978.ZerolBevelGearSetCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearSetCompoundSystemDeflection]

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
    ) -> "Iterable[_2891.CycloidalAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2893.CycloidalDiscCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscCompoundSystemDeflection]

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
    ) -> "Iterable[_2938.RingPinsCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RingPinsCompoundSystemDeflection]

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
    ) -> "Iterable[_2929.PartToPartShearCouplingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingCompoundSystemDeflection]

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
    ) -> "Iterable[_2931.PartToPartShearCouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2858.BeltDriveCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BeltDriveCompoundSystemDeflection]

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
    ) -> "Iterable[_2869.ClutchCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ClutchCompoundSystemDeflection]

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
    ) -> "Iterable[_2871.ClutchHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ClutchHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2874.ConceptCouplingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingCompoundSystemDeflection]

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
    ) -> "Iterable[_2876.ConceptCouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2885.CouplingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CouplingCompoundSystemDeflection]

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
    ) -> "Iterable[_2887.CouplingHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CouplingHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2889.CVTCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CVTCompoundSystemDeflection]

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
    ) -> "Iterable[_2890.CVTPulleyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CVTPulleyCompoundSystemDeflection]

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
    ) -> "Iterable[_2937.PulleyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PulleyCompoundSystemDeflection]

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
    ) -> "Iterable[_2946.ShaftHubConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftHubConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2941.RollingRingCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingCompoundSystemDeflection]

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
    ) -> "Iterable[_2940.RollingRingAssemblyCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingAssemblyCompoundSystemDeflection]

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
    ) -> "Iterable[_2952.SpringDamperCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpringDamperCompoundSystemDeflection]

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
    ) -> "Iterable[_2954.SpringDamperHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpringDamperHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2963.SynchroniserCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SynchroniserCompoundSystemDeflection]

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
    ) -> "Iterable[_2964.SynchroniserHalfCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SynchroniserHalfCompoundSystemDeflection]

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
    ) -> "Iterable[_2965.SynchroniserPartCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SynchroniserPartCompoundSystemDeflection]

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
    ) -> "Iterable[_2966.SynchroniserSleeveCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SynchroniserSleeveCompoundSystemDeflection]

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
    ) -> "Iterable[_2967.TorqueConverterCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.TorqueConverterCompoundSystemDeflection]

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
    ) -> "Iterable[_2969.TorqueConverterPumpCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.TorqueConverterPumpCompoundSystemDeflection]

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
    ) -> "Iterable[_2970.TorqueConverterTurbineCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.TorqueConverterTurbineCompoundSystemDeflection]

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
    ) -> "Iterable[_2947.ShaftToMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftToMountableComponentConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2888.CVTBeltConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CVTBeltConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2857.BeltConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BeltConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2872.CoaxialConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CoaxialConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2883.ConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2914.InterMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.InterMountableComponentConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2932.PlanetaryConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PlanetaryConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2942.RollingRingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2851.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2860.BevelDifferentialGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelDifferentialGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2878.ConceptGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2903.FaceGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.FaceGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2956.StraightBevelDiffGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelDiffGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2865.BevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.BevelGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2881.ConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConicalGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2853.AGMAGleasonConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.AGMAGleasonConicalGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2896.CylindricalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2912.HypoidGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.HypoidGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2916.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection]

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
    ) -> (
        "Iterable[_2919.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2922.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2950.SpiralBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.SpiralBevelGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2959.StraightBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.StraightBevelGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2974.WormGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.WormGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2977.ZerolBevelGearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ZerolBevelGearMeshCompoundSystemDeflection]

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
    ) -> "Iterable[_2908.GearMeshCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.GearMeshCompoundSystemDeflection]

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
    ) -> (
        "Iterable[_2892.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection]"
    ):
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2894.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2939.RingPinsToDiscConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.RingPinsToDiscConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2930.PartToPartShearCouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.PartToPartShearCouplingConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2870.ClutchConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ClutchConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2875.ConceptCouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.ConceptCouplingConnectionCompoundSystemDeflection]

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
    ) -> "Iterable[_2886.CouplingConnectionCompoundSystemDeflection]":
        """Iterable[mastapy.system_model.analyses_and_results.system_deflections.compound.CouplingConnectionCompoundSystemDeflection]

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
    ) -> "CompoundSystemDeflectionAnalysis._Cast_CompoundSystemDeflectionAnalysis":
        return self._Cast_CompoundSystemDeflectionAnalysis(self)

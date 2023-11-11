"""DesignEntity"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2197
    from mastapy.utility.model_validation import _1791, _1790
    from mastapy.utility.scripting import _1738


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2262

            return self._parent._cast(_2262.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2265

            return self._parent._cast(_2265.BeltConnection)

        @property
        def coaxial_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2266

            return self._parent._cast(_2266.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def cvt_belt_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.InterMountableComponentConnection)

        @property
        def planetary_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.PlanetaryConnection)

        @property
        def rolling_ring_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2296

            return self._parent._cast(_2296.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2298

            return self._parent._cast(_2298.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2300

            return self._parent._cast(_2300.BevelGearMesh)

        @property
        def concept_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.ConceptGearMesh)

        @property
        def conical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def hypoid_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2332

            return self._parent._cast(_2332.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2335

            return self._parent._cast(_2335.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2338

            return self._parent._cast(_2338.RingPinsToDiscConnection)

        @property
        def clutch_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2339

            return self._parent._cast(_2339.ClutchConnection)

        @property
        def concept_coupling_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2341

            return self._parent._cast(_2341.ConceptCouplingConnection)

        @property
        def coupling_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2343

            return self._parent._cast(_2343.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2345

            return self._parent._cast(_2345.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2347

            return self._parent._cast(_2347.SpringDamperConnection)

        @property
        def torque_converter_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2430

            return self._parent._cast(_2430.Assembly)

        @property
        def abstract_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.AbstractAssembly)

        @property
        def abstract_shaft(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2432

            return self._parent._cast(_2432.AbstractShaft)

        @property
        def abstract_shaft_or_housing(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2433

            return self._parent._cast(_2433.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2436

            return self._parent._cast(_2436.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2439

            return self._parent._cast(_2439.Bolt)

        @property
        def bolted_joint(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2440

            return self._parent._cast(_2440.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2445

            return self._parent._cast(_2445.Datum)

        @property
        def external_cad_model(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2449

            return self._parent._cast(_2449.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2450

            return self._parent._cast(_2450.FEPart)

        @property
        def flexible_pin_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.MassDisc)

        @property
        def measurement_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.MeasurementComponent)

        @property
        def mountable_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def planet_carrier(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PowerLoad)

        @property
        def root_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.RootAssembly)

        @property
        def specialised_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.UnbalancedMass)

        @property
        def virtual_component(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.shaft_model import _2479

            return self._parent._cast(_2479.Shaft)

        @property
        def agma_gleason_conical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2510

            return self._parent._cast(_2510.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelGear)

        @property
        def bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelGearSet)

        @property
        def concept_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.ConceptGear)

        @property
        def concept_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.ConceptGearSet)

        @property
        def conical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConicalGear)

        @property
        def conical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGearSet)

        @property
        def cylindrical_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.FaceGear)

        @property
        def face_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.HypoidGear)

        @property
        def hypoid_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelGear)

        @property
        def straight_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.WormGear)

        @property
        def worm_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.WormGearSet)

        @property
        def zerol_bevel_gear(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2565

            return self._parent._cast(_2565.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2566

            return self._parent._cast(_2566.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.cycloidal import _2567

            return self._parent._cast(_2567.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2573

            return self._parent._cast(_2573.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2575

            return self._parent._cast(_2575.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.ClutchHalf)

        @property
        def concept_coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2578

            return self._parent._cast(_2578.ConceptCoupling)

        @property
        def concept_coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2580

            return self._parent._cast(_2580.Coupling)

        @property
        def coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2583

            return self._parent._cast(_2583.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CVTPulley)

        @property
        def part_to_part_shear_coupling(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2585

            return self._parent._cast(_2585.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.Pulley)

        @property
        def rolling_ring(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2593

            return self._parent._cast(_2593.RollingRing)

        @property
        def rolling_ring_assembly(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.ShaftHubConnection)

        @property
        def spring_damper(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2597

            return self._parent._cast(_2597.SpringDamper)

        @property
        def spring_damper_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.SpringDamperHalf)

        @property
        def synchroniser(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.Synchroniser)

        @property
        def synchroniser_half(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.SynchroniserHalf)

        @property
        def synchroniser_part(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SynchroniserSleeve)

        @property
        def torque_converter(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.TorqueConverter)

        @property
        def torque_converter_pump(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.TorqueConverterPump)

        @property
        def torque_converter_turbine(self: "DesignEntity._Cast_DesignEntity"):
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def design_properties(self: Self) -> "_2197.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1791.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1790.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1738.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)

"""MountableComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432, _2442
    from mastapy.system_model.connections_and_sockets import _2269, _2273, _2266


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2441.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(self: "MountableComponent._Cast_MountableComponent"):
            return self._parent._cast(_2441.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def bearing(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2436

            return self._parent._cast(_2436.Bearing)

        @property
        def connector(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Connector)

        @property
        def mass_disc(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.MassDisc)

        @property
        def measurement_component(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.MeasurementComponent)

        @property
        def oil_seal(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.OilSeal)

        @property
        def planet_carrier(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.PlanetCarrier)

        @property
        def point_load(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.PointLoad)

        @property
        def power_load(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PowerLoad)

        @property
        def unbalanced_mass(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.UnbalancedMass)

        @property
        def virtual_component(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model import _2476

            return self._parent._cast(_2476.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2510

            return self._parent._cast(_2510.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2512

            return self._parent._cast(_2512.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2514

            return self._parent._cast(_2514.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelGear)

        @property
        def concept_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.ConceptGear)

        @property
        def conical_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConicalGear)

        @property
        def cylindrical_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.CylindricalPlanetGear)

        @property
        def face_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.Gear)

        @property
        def hypoid_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelSunGear)

        @property
        def worm_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.WormGear)

        @property
        def zerol_bevel_gear(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.ZerolBevelGear)

        @property
        def ring_pins(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.cycloidal import _2567

            return self._parent._cast(_2567.RingPins)

        @property
        def clutch_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2576

            return self._parent._cast(_2576.ClutchHalf)

        @property
        def concept_coupling_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ConceptCouplingHalf)

        @property
        def coupling_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2581

            return self._parent._cast(_2581.CouplingHalf)

        @property
        def cvt_pulley(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2584

            return self._parent._cast(_2584.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.couplings import _2586

            return self._parent._cast(_2586.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.Pulley)

        @property
        def rolling_ring(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2593

            return self._parent._cast(_2593.RollingRing)

        @property
        def shaft_hub_connection(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2595

            return self._parent._cast(_2595.ShaftHubConnection)

        @property
        def spring_damper_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.SpringDamperHalf)

        @property
        def synchroniser_half(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.SynchroniserHalf)

        @property
        def synchroniser_part(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2603

            return self._parent._cast(_2603.SynchroniserSleeve)

        @property
        def torque_converter_pump(self: "MountableComponent._Cast_MountableComponent"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ):
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2432.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2269.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2273.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2432.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2432.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2442.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)

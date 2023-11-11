"""InterMountableComponentConnection"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2269
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


Self = TypeVar("Self", bound="InterMountableComponentConnection")


class InterMountableComponentConnection(_2269.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterMountableComponentConnection")

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            parent: "InterMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2265

            return self._parent._cast(_2265.BeltConnection)

        @property
        def cvt_belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.CVTBeltConnection)

        @property
        def rolling_ring_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.RollingRingConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2296

            return self._parent._cast(_2296.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2298

            return self._parent._cast(_2298.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2300

            return self._parent._cast(_2300.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2302

            return self._parent._cast(_2302.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.FaceGearMesh)

        @property
        def gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ZerolBevelGearMesh)

        @property
        def ring_pins_to_disc_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2338

            return self._parent._cast(_2338.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2339

            return self._parent._cast(_2339.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2341

            return self._parent._cast(_2341.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2343

            return self._parent._cast(_2343.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2345

            return self._parent._cast(_2345.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2347

            return self._parent._cast(_2347.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.TorqueConverterConnection)

        @property
        def inter_mountable_component_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "InterMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "InterMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnection._Cast_InterMountableComponentConnection":
        return self._Cast_InterMountableComponentConnection(self)

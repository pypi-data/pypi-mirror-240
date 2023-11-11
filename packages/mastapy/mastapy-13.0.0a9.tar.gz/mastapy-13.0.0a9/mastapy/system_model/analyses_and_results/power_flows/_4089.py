"""GearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4096
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.gears.rating import _358
    from mastapy.system_model.analyses_and_results.power_flows import _4150


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshPowerFlow",)


Self = TypeVar("Self", bound="GearMeshPowerFlow")


class GearMeshPowerFlow(_4096.InterMountableComponentConnectionPowerFlow):
    """GearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshPowerFlow")

    class _Cast_GearMeshPowerFlow:
        """Special nested class for casting GearMeshPowerFlow to subclasses."""

        def __init__(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
            parent: "GearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            return self._parent._cast(_4096.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelGearMeshPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConicalGearMeshPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4077

            return self._parent._cast(_4077.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.FaceGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4093

            return self._parent._cast(_4093.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(
                _4097.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4100

            return self._parent._cast(
                _4100.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelGearMeshPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.ZerolBevelGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ) -> "GearMeshPowerFlow":
            return self._parent

        def __getattr__(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_tooth_passing_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_tooth_passing_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2310.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_358.GearMeshRating":
        """mastapy.gears.rating.GearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_passing_harmonics(self: Self) -> "List[_4150.ToothPassingHarmonic]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ToothPassingHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearMeshPowerFlow._Cast_GearMeshPowerFlow":
        return self._Cast_GearMeshPowerFlow(self)

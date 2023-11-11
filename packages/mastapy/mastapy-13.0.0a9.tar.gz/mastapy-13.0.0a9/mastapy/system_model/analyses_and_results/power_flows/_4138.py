"""StraightBevelDiffGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4045
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelDiffGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel_diff import _396
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshPowerFlow")


class StraightBevelDiffGearMeshPowerFlow(_4045.BevelGearMeshPowerFlow):
    """StraightBevelDiffGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMeshPowerFlow")

    class _Cast_StraightBevelDiffGearMeshPowerFlow:
        """Special nested class for casting StraightBevelDiffGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
            parent: "StraightBevelDiffGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            return self._parent._cast(_4045.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
        ) -> "StraightBevelDiffGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearMeshPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_396.StraightBevelDiffGearMeshRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_396.StraightBevelDiffGearMeshRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow":
        return self._Cast_StraightBevelDiffGearMeshPowerFlow(self)

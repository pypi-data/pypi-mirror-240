"""ZerolBevelGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ZerolBevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _367
    from mastapy.system_model.connections_and_sockets.gears import _2328
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.power_flows import _4160


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshSystemDeflection")


class ZerolBevelGearMeshSystemDeflection(_2703.BevelGearMeshSystemDeflection):
    """ZerolBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshSystemDeflection")

    class _Cast_ZerolBevelGearMeshSystemDeflection:
        """Special nested class for casting ZerolBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
            parent: "ZerolBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            return self._parent._cast(_2703.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(_2686.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(
                _2764.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
        ) -> "ZerolBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_367.ZerolBevelGearMeshRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_367.ZerolBevelGearMeshRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2328.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6983.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4160.ZerolBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshSystemDeflection._Cast_ZerolBevelGearMeshSystemDeflection":
        return self._Cast_ZerolBevelGearMeshSystemDeflection(self)

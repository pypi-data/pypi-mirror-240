"""CylindricalGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CylindricalGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _456
    from mastapy.system_model.connections_and_sockets.gears import _2306
    from mastapy.system_model.analyses_and_results.static_loads import _6860


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshPowerFlow",)


Self = TypeVar("Self", bound="CylindricalGearMeshPowerFlow")


class CylindricalGearMeshPowerFlow(_4089.GearMeshPowerFlow):
    """CylindricalGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshPowerFlow")

    class _Cast_CylindricalGearMeshPowerFlow:
        """Special nested class for casting CylindricalGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
            parent: "CylindricalGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_power_flow(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            return self._parent._cast(_4089.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
        ) -> "CylindricalGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_456.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_456.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2306.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6860.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

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
    ) -> "CylindricalGearMeshPowerFlow._Cast_CylindricalGearMeshPowerFlow":
        return self._Cast_CylindricalGearMeshPowerFlow(self)

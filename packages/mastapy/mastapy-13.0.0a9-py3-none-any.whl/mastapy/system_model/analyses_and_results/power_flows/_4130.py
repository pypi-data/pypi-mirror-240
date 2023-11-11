"""ShaftToMountableComponentConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4032
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ShaftToMountableComponentConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionPowerFlow",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionPowerFlow")


class ShaftToMountableComponentConnectionPowerFlow(
    _4032.AbstractShaftToMountableComponentConnectionPowerFlow
):
    """ShaftToMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionPowerFlow"
    )

    class _Cast_ShaftToMountableComponentConnectionPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
            parent: "ShaftToMountableComponentConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            return self._parent._cast(
                _4032.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.CoaxialConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(
                _4073.CycloidalDiscCentralBearingConnectionPowerFlow
            )

        @property
        def planetary_connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PlanetaryConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
        ) -> "ShaftToMountableComponentConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow",
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
        self: Self,
        instance_to_wrap: "ShaftToMountableComponentConnectionPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2292.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow":
        return self._Cast_ShaftToMountableComponentConnectionPowerFlow(self)

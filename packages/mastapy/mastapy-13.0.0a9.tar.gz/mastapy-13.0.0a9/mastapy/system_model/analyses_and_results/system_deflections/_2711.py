"""CoaxialConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CoaxialConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.static_loads import _6833
    from mastapy.system_model.analyses_and_results.power_flows import _4053


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionSystemDeflection")


class CoaxialConnectionSystemDeflection(
    _2802.ShaftToMountableComponentConnectionSystemDeflection
):
    """CoaxialConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionSystemDeflection")

    class _Cast_CoaxialConnectionSystemDeflection:
        """Special nested class for casting CoaxialConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
            parent: "CoaxialConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            return self._parent._cast(
                _2802.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(
                _2685.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(
                _2733.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def coaxial_connection_system_deflection(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
        ) -> "CoaxialConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6833.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4053.CoaxialConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CoaxialConnectionPowerFlow

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
    ) -> "CoaxialConnectionSystemDeflection._Cast_CoaxialConnectionSystemDeflection":
        return self._Cast_CoaxialConnectionSystemDeflection(self)

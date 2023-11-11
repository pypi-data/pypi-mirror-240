"""CycloidalDiscPlanetaryBearingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6857
    from mastapy.system_model.analyses_and_results.power_flows import _4074


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionSystemDeflection")


class CycloidalDiscPlanetaryBearingConnectionSystemDeflection(
    _2685.AbstractShaftToMountableComponentConnectionSystemDeflection
):
    """CycloidalDiscPlanetaryBearingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
            parent: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            return self._parent._cast(
                _2685.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
        ) -> "CycloidalDiscPlanetaryBearingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2335.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6857.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4074.CycloidalDiscPlanetaryBearingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CycloidalDiscPlanetaryBearingConnectionPowerFlow

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection(self)

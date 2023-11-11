"""AbstractShaftToMountableComponentConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2724
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262
    from mastapy.system_model.analyses_and_results.power_flows import _4032


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionSystemDeflection",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionSystemDeflection"
)


class AbstractShaftToMountableComponentConnectionSystemDeflection(
    _2724.ConnectionSystemDeflection
):
    """AbstractShaftToMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
            parent: "AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.CoaxialConnectionSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(
                _2733.CycloidalDiscCentralBearingConnectionSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(
                _2734.CycloidalDiscPlanetaryBearingConnectionSystemDeflection
            )

        @property
        def planetary_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.PlanetaryConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(
                _2802.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
        ) -> "AbstractShaftToMountableComponentConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2262.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4032.AbstractShaftToMountableComponentConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftToMountableComponentConnectionPowerFlow

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
    ) -> "AbstractShaftToMountableComponentConnectionSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection":
        return self._Cast_AbstractShaftToMountableComponentConnectionSystemDeflection(
            self
        )

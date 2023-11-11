"""PlanetaryConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3078,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PlanetaryConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2284
    from mastapy.system_model.analyses_and_results.static_loads import _6929


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PlanetaryConnectionSteadyStateSynchronousResponse")


class PlanetaryConnectionSteadyStateSynchronousResponse(
    _3078.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
):
    """PlanetaryConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_PlanetaryConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetaryConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
            parent: "PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3078.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
        ) -> "PlanetaryConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetaryConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2284.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6929.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

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
    ) -> "PlanetaryConnectionSteadyStateSynchronousResponse._Cast_PlanetaryConnectionSteadyStateSynchronousResponse":
        return self._Cast_PlanetaryConnectionSteadyStateSynchronousResponse(self)

"""AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3015,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
)


class AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
    _3015.ConnectionSteadyStateSynchronousResponse
):
    """AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
            parent: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3004,
            )

            return self._parent._cast(
                _3004.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(
                _3024.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3064,
            )

            return self._parent._cast(
                _3064.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(
                _3078.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> (
            "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
        return self._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
            self
        )

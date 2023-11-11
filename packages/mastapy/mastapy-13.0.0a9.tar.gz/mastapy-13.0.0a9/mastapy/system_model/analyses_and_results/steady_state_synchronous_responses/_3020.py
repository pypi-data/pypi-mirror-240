"""CVTBeltConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2989,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CVTBeltConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTBeltConnectionSteadyStateSynchronousResponse")


class CVTBeltConnectionSteadyStateSynchronousResponse(
    _2989.BeltConnectionSteadyStateSynchronousResponse
):
    """CVTBeltConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_CVTBeltConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CVTBeltConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
            parent: "CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2989.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
        ) -> "CVTBeltConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CVTBeltConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2270.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

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
    ) -> "CVTBeltConnectionSteadyStateSynchronousResponse._Cast_CVTBeltConnectionSteadyStateSynchronousResponse":
        return self._Cast_CVTBeltConnectionSteadyStateSynchronousResponse(self)

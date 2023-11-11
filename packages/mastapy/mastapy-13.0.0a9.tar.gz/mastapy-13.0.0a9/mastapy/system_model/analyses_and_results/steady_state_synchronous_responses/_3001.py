"""ClutchConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ClutchConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2339
    from mastapy.system_model.analyses_and_results.static_loads import _6829


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ClutchConnectionSteadyStateSynchronousResponse")


class ClutchConnectionSteadyStateSynchronousResponse(
    _3017.CouplingConnectionSteadyStateSynchronousResponse
):
    """ClutchConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_ClutchConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ClutchConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
            parent: "ClutchConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3017.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
        ) -> "ClutchConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ClutchConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2339.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6829.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

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
    ) -> "ClutchConnectionSteadyStateSynchronousResponse._Cast_ClutchConnectionSteadyStateSynchronousResponse":
        return self._Cast_ClutchConnectionSteadyStateSynchronousResponse(self)

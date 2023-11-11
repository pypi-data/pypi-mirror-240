"""ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3116,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3078,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3116.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3116.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> (
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse"
        ):
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> (
        "List[_3078.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> (
        "List[_3078.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )

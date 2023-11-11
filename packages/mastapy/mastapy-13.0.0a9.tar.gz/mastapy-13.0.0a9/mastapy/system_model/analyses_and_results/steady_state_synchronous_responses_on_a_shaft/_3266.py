"""CoaxialConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3339,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.static_loads import _6833


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CoaxialConnectionSteadyStateSynchronousResponseOnAShaft")


class CoaxialConnectionSteadyStateSynchronousResponseOnAShaft(
    _3339.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CoaxialConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CoaxialConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3339.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3245,
            )

            return self._parent._cast(
                _3245.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CoaxialConnectionSteadyStateSynchronousResponseOnAShaft(self)

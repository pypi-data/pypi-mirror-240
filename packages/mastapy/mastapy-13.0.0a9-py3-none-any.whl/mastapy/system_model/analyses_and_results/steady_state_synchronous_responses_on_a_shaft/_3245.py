"""AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3277,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)


class AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
    _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
):
    """AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3266,
            )

            return self._parent._cast(
                _3266.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )

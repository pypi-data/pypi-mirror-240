"""RingPinsCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3190,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "RingPinsCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3070,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RingPinsCompoundSteadyStateSynchronousResponse")


class RingPinsCompoundSteadyStateSynchronousResponse(
    _3190.MountableComponentCompoundSteadyStateSynchronousResponse
):
    """RingPinsCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_RingPinsCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting RingPinsCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
            parent: "RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
        ) -> "RingPinsCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "RingPinsCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3070.RingPinsSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RingPinsSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3070.RingPinsSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RingPinsSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsCompoundSteadyStateSynchronousResponse._Cast_RingPinsCompoundSteadyStateSynchronousResponse":
        return self._Cast_RingPinsCompoundSteadyStateSynchronousResponse(self)

"""ClutchHalfCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3152,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ClutchHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3002,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ClutchHalfCompoundSteadyStateSynchronousResponse")


class ClutchHalfCompoundSteadyStateSynchronousResponse(
    _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """ClutchHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ClutchHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ClutchHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
            parent: "ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
        ) -> "ClutchHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ClutchHalfCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

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
    ) -> "List[_3002.ClutchHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ClutchHalfSteadyStateSynchronousResponse]

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
    ) -> "List[_3002.ClutchHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ClutchHalfSteadyStateSynchronousResponse]

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
    ) -> "ClutchHalfCompoundSteadyStateSynchronousResponse._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_ClutchHalfCompoundSteadyStateSynchronousResponse(self)

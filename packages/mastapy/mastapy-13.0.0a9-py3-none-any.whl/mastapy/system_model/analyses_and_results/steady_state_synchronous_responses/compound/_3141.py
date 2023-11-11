"""ConceptCouplingHalfCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3152,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3007,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="ConceptCouplingHalfCompoundSteadyStateSynchronousResponse"
)


class ConceptCouplingHalfCompoundSteadyStateSynchronousResponse(
    _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """ConceptCouplingHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
            parent: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2579.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

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
    ) -> "List[_3007.ConceptCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingHalfSteadyStateSynchronousResponse]

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
    ) -> "List[_3007.ConceptCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingHalfSteadyStateSynchronousResponse]

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
    ) -> "ConceptCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponse(
            self
        )

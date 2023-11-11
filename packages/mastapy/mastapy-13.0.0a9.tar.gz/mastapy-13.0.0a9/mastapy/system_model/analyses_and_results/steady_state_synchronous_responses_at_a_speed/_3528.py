"""ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3539,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6836


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"
)


class ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed(
    _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
            parent: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    def component_load_case(self: Self) -> "_6836.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed(
            self
        )

"""ConceptGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3171,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConceptGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3011,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptGearCompoundSteadyStateSynchronousResponse")


class ConceptGearCompoundSteadyStateSynchronousResponse(
    _3171.GearCompoundSteadyStateSynchronousResponse
):
    """ConceptGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
            parent: "ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3171.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
        ) -> "ConceptGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2518.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

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
    ) -> "List[_3011.ConceptGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3011.ConceptGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearSteadyStateSynchronousResponse]

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
    ) -> "ConceptGearCompoundSteadyStateSynchronousResponse._Cast_ConceptGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConceptGearCompoundSteadyStateSynchronousResponse(self)

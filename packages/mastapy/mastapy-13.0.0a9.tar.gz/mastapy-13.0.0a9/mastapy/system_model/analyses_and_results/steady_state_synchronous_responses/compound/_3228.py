"""SynchroniserPartCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3152,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SynchroniserPartCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3098,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundSteadyStateSynchronousResponse")


class SynchroniserPartCompoundSteadyStateSynchronousResponse(
    _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """SynchroniserPartCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserPartCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
            parent: "SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
        ) -> "SynchroniserPartCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserPartCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3098.SynchroniserPartSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserPartSteadyStateSynchronousResponse]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3098.SynchroniserPartSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserPartSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundSteadyStateSynchronousResponse._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserPartCompoundSteadyStateSynchronousResponse(self)

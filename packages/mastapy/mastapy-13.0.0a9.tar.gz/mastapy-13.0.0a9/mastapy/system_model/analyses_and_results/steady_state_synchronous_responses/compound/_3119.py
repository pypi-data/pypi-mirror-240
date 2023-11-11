"""AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3147,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2985,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse"
)


class AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse(
    _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3113,
            )

            return self._parent._cast(
                _3113.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse(
                self
            )
        )

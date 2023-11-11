"""BevelGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3119,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2997,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearSetCompoundSteadyStateSynchronousResponse")


class BevelGearSetCompoundSteadyStateSynchronousResponse(
    _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
):
    """BevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3113,
            )

            return self._parent._cast(
                _3113.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2997.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

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
    ) -> "List[_2997.BevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSetSteadyStateSynchronousResponse]

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
    ) -> "BevelGearSetCompoundSteadyStateSynchronousResponse._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearSetCompoundSteadyStateSynchronousResponse(self)

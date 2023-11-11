"""BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3124,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2994,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse"
)


class BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse(
    _3124.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
):
    """BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
            parent: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3124.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(_3171.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2994.BevelDifferentialPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "List[_2994.BevelDifferentialPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse(
            self
        )

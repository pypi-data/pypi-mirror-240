"""BevelDifferentialGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3129,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2993,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearCompoundSteadyStateSynchronousResponse"
)


class BevelDifferentialGearCompoundSteadyStateSynchronousResponse(
    _3129.BevelGearCompoundSteadyStateSynchronousResponse
):
    """BevelDifferentialGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
            parent: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3129.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(_3171.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3127,
            )

            return self._parent._cast(
                _3127.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2512.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "List[_2993.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

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
    ) -> "List[_2993.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

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
    ) -> "BevelDifferentialGearCompoundSteadyStateSynchronousResponse._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialGearCompoundSteadyStateSynchronousResponse(
            self
        )

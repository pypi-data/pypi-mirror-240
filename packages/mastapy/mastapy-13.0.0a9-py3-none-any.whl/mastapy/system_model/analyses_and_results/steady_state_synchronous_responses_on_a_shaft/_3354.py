"""StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3350,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft(
    _3350.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3350.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(_3302.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft(
            self
        )

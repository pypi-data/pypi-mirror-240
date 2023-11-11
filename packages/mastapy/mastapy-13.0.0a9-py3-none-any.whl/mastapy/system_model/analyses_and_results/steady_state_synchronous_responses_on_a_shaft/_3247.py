"""AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3275,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3275.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3275.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )

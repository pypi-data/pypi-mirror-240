"""BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3514,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"
)


class BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed(
    _3514.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3514.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(_3561.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )

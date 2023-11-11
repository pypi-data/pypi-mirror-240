"""SynchroniserPartSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3539,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserPartSteadyStateSynchronousResponseAtASpeed")


class SynchroniserPartSteadyStateSynchronousResponseAtASpeed(
    _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """SynchroniserPartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SynchroniserPartSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
            parent: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
        ) -> "SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SynchroniserPartSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SynchroniserPartSteadyStateSynchronousResponseAtASpeed(self)

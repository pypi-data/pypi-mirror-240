"""PulleySteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3539,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PulleySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6937


__docformat__ = "restructuredtext en"
__all__ = ("PulleySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PulleySteadyStateSynchronousResponseAtASpeed")


class PulleySteadyStateSynchronousResponseAtASpeed(
    _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
):
    """PulleySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PulleySteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_PulleySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PulleySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
            parent: "PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "PulleySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PulleySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6937.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PulleySteadyStateSynchronousResponseAtASpeed._Cast_PulleySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PulleySteadyStateSynchronousResponseAtASpeed(self)

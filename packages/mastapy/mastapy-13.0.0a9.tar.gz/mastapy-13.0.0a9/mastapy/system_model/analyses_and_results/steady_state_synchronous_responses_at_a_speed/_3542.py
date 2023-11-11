"""CVTPulleySteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3589,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CVTPulleySteadyStateSynchronousResponseAtASpeed")


class CVTPulleySteadyStateSynchronousResponseAtASpeed(
    _3589.PulleySteadyStateSynchronousResponseAtASpeed
):
    """CVTPulleySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CVTPulleySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
            parent: "CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3589.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
        ) -> "CVTPulleySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CVTPulleySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleySteadyStateSynchronousResponseAtASpeed._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CVTPulleySteadyStateSynchronousResponseAtASpeed(self)

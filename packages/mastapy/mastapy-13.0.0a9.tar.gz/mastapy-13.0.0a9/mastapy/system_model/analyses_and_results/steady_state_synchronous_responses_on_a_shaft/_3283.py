"""CVTPulleySteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3330,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CVTPulleySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CVTPulleySteadyStateSynchronousResponseOnAShaft")


class CVTPulleySteadyStateSynchronousResponseOnAShaft(
    _3330.PulleySteadyStateSynchronousResponseOnAShaft
):
    """CVTPulleySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CVTPulleySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
            parent: "CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3330.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
        ) -> "CVTPulleySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CVTPulleySteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "CVTPulleySteadyStateSynchronousResponseOnAShaft._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CVTPulleySteadyStateSynchronousResponseOnAShaft(self)

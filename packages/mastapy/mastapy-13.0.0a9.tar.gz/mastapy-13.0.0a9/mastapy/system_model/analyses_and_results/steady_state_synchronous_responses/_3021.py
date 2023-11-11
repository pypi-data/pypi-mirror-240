"""CVTPulleySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CVTPulleySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTPulleySteadyStateSynchronousResponse")


class CVTPulleySteadyStateSynchronousResponse(
    _3069.PulleySteadyStateSynchronousResponse
):
    """CVTPulleySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleySteadyStateSynchronousResponse"
    )

    class _Cast_CVTPulleySteadyStateSynchronousResponse:
        """Special nested class for casting CVTPulleySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
            parent: "CVTPulleySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def pulley_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3069.PulleySteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
        ) -> "CVTPulleySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CVTPulleySteadyStateSynchronousResponse.TYPE"
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
    ) -> "CVTPulleySteadyStateSynchronousResponse._Cast_CVTPulleySteadyStateSynchronousResponse":
        return self._Cast_CVTPulleySteadyStateSynchronousResponse(self)

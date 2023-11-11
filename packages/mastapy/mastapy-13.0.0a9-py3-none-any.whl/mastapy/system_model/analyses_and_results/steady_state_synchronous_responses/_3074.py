"""RollingRingSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3018,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "RollingRingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2593
    from mastapy.system_model.analyses_and_results.static_loads import _6944


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RollingRingSteadyStateSynchronousResponse")


class RollingRingSteadyStateSynchronousResponse(
    _3018.CouplingHalfSteadyStateSynchronousResponse
):
    """RollingRingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingSteadyStateSynchronousResponse"
    )

    class _Cast_RollingRingSteadyStateSynchronousResponse:
        """Special nested class for casting RollingRingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
            parent: "RollingRingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3018.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
        ) -> "RollingRingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "RollingRingSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2593.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6944.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.RollingRingSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingSteadyStateSynchronousResponse._Cast_RollingRingSteadyStateSynchronousResponse":
        return self._Cast_RollingRingSteadyStateSynchronousResponse(self)

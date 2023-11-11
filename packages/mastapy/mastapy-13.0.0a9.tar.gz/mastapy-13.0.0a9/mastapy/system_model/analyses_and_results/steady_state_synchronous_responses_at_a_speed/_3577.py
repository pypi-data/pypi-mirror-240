"""MeasurementComponentSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3624,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="MeasurementComponentSteadyStateSynchronousResponseAtASpeed"
)


class MeasurementComponentSteadyStateSynchronousResponseAtASpeed(
    _3624.VirtualComponentSteadyStateSynchronousResponseAtASpeed
):
    """MeasurementComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting MeasurementComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3624.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "MeasurementComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6919.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentSteadyStateSynchronousResponseAtASpeed._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_MeasurementComponentSteadyStateSynchronousResponseAtASpeed(
            self
        )

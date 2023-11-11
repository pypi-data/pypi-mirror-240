"""MeasurementComponentModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="MeasurementComponentModalAnalysisAtASpeed")


class MeasurementComponentModalAnalysisAtASpeed(
    _5236.VirtualComponentModalAnalysisAtASpeed
):
    """MeasurementComponentModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentModalAnalysisAtASpeed"
    )

    class _Cast_MeasurementComponentModalAnalysisAtASpeed:
        """Special nested class for casting MeasurementComponentModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
            parent: "MeasurementComponentModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5236.VirtualComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
        ) -> "MeasurementComponentModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "MeasurementComponentModalAnalysisAtASpeed.TYPE"
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
    ) -> "MeasurementComponentModalAnalysisAtASpeed._Cast_MeasurementComponentModalAnalysisAtASpeed":
        return self._Cast_MeasurementComponentModalAnalysisAtASpeed(self)

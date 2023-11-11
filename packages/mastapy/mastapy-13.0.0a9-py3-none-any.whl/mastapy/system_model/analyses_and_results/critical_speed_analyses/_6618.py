"""MeasurementComponentCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "MeasurementComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentCriticalSpeedAnalysis")


class MeasurementComponentCriticalSpeedAnalysis(
    _6664.VirtualComponentCriticalSpeedAnalysis
):
    """MeasurementComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCriticalSpeedAnalysis"
    )

    class _Cast_MeasurementComponentCriticalSpeedAnalysis:
        """Special nested class for casting MeasurementComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
            parent: "MeasurementComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6664.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
        ) -> "MeasurementComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentCriticalSpeedAnalysis.TYPE"
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
    ) -> "MeasurementComponentCriticalSpeedAnalysis._Cast_MeasurementComponentCriticalSpeedAnalysis":
        return self._Cast_MeasurementComponentCriticalSpeedAnalysis(self)

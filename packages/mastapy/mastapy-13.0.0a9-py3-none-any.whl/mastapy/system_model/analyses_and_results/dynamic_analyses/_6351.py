"""MeasurementComponentDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "MeasurementComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentDynamicAnalysis")


class MeasurementComponentDynamicAnalysis(_6397.VirtualComponentDynamicAnalysis):
    """MeasurementComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementComponentDynamicAnalysis")

    class _Cast_MeasurementComponentDynamicAnalysis:
        """Special nested class for casting MeasurementComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
            parent: "MeasurementComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_dynamic_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            return self._parent._cast(_6397.VirtualComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
        ) -> "MeasurementComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentDynamicAnalysis.TYPE"
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
    ) -> (
        "MeasurementComponentDynamicAnalysis._Cast_MeasurementComponentDynamicAnalysis"
    ):
        return self._Cast_MeasurementComponentDynamicAnalysis(self)

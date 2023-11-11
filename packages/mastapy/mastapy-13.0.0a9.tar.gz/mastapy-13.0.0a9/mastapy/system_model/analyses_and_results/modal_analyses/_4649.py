"""MeasurementComponentModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "MeasurementComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919
    from mastapy.system_model.analyses_and_results.system_deflections import _2777


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentModalAnalysis",)


Self = TypeVar("Self", bound="MeasurementComponentModalAnalysis")


class MeasurementComponentModalAnalysis(_4702.VirtualComponentModalAnalysis):
    """MeasurementComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementComponentModalAnalysis")

    class _Cast_MeasurementComponentModalAnalysis:
        """Special nested class for casting MeasurementComponentModalAnalysis to subclasses."""

        def __init__(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
            parent: "MeasurementComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            return self._parent._cast(_4702.VirtualComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
        ) -> "MeasurementComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis",
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
        self: Self, instance_to_wrap: "MeasurementComponentModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2777.MeasurementComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentModalAnalysis._Cast_MeasurementComponentModalAnalysis":
        return self._Cast_MeasurementComponentModalAnalysis(self)

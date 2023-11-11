"""ShaftModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "ShaftModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2479
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.system_deflections import _2801


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalAnalysis",)


Self = TypeVar("Self", bound="ShaftModalAnalysis")


class ShaftModalAnalysis(_4569.AbstractShaftModalAnalysis):
    """ShaftModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalAnalysis")

    class _Cast_ShaftModalAnalysis:
        """Special nested class for casting ShaftModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
            parent: "ShaftModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ):
            return self._parent._cast(_4569.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570

            return self._parent._cast(_4570.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def shaft_modal_analysis(
            self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis",
        ) -> "ShaftModalAnalysis":
            return self._parent

        def __getattr__(self: "ShaftModalAnalysis._Cast_ShaftModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6947.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2801.ShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis]

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
    def cast_to(self: Self) -> "ShaftModalAnalysis._Cast_ShaftModalAnalysis":
        return self._Cast_ShaftModalAnalysis(self)

"""CycloidalDiscModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4569
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CycloidalDiscModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2566
    from mastapy.system_model.analyses_and_results.static_loads import _6856
    from mastapy.system_model.analyses_and_results.system_deflections import _2735


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscModalAnalysis")


class CycloidalDiscModalAnalysis(_4569.AbstractShaftModalAnalysis):
    """CycloidalDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscModalAnalysis")

    class _Cast_CycloidalDiscModalAnalysis:
        """Special nested class for casting CycloidalDiscModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            parent: "CycloidalDiscModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            return self._parent._cast(_4569.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570

            return self._parent._cast(_4570.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
        ) -> "CycloidalDiscModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2566.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6856.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2735.CycloidalDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscSystemDeflection

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
    ) -> "CycloidalDiscModalAnalysis._Cast_CycloidalDiscModalAnalysis":
        return self._Cast_CycloidalDiscModalAnalysis(self)

"""ClutchModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "ClutchModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.system_deflections import _2710


__docformat__ = "restructuredtext en"
__all__ = ("ClutchModalAnalysis",)


Self = TypeVar("Self", bound="ClutchModalAnalysis")


class ClutchModalAnalysis(_4608.CouplingModalAnalysis):
    """ClutchModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchModalAnalysis")

    class _Cast_ClutchModalAnalysis:
        """Special nested class for casting ClutchModalAnalysis to subclasses."""

        def __init__(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
            parent: "ClutchModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            return self._parent._cast(_4608.CouplingModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis",
        ) -> "ClutchModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchModalAnalysis._Cast_ClutchModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6831.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2710.ClutchSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchModalAnalysis._Cast_ClutchModalAnalysis":
        return self._Cast_ClutchModalAnalysis(self)

"""RootAssemblyHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "RootAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5763, _5757
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5872,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2797


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyHarmonicAnalysis")


class RootAssemblyHarmonicAnalysis(_5682.AssemblyHarmonicAnalysis):
    """RootAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyHarmonicAnalysis")

    class _Cast_RootAssemblyHarmonicAnalysis:
        """Special nested class for casting RootAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
            parent: "RootAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_harmonic_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            return self._parent._cast(_5682.AssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
        ) -> "RootAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2471.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def export(self: Self) -> "_5763.HarmonicAnalysisRootAssemblyExportOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisRootAssemblyExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_inputs(self: Self) -> "_5757.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(
        self: Self,
    ) -> "_5872.RootAssemblyHarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.RootAssemblyHarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2797.RootAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection

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
    ) -> "RootAssemblyHarmonicAnalysis._Cast_RootAssemblyHarmonicAnalysis":
        return self._Cast_RootAssemblyHarmonicAnalysis(self)

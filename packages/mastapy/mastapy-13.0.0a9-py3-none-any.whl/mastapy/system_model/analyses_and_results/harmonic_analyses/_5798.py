"""RollingRingAssemblyHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "RollingRingAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.system_deflections import _2794


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyHarmonicAnalysis")


class RollingRingAssemblyHarmonicAnalysis(_5806.SpecialisedAssemblyHarmonicAnalysis):
    """RollingRingAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyHarmonicAnalysis")

    class _Cast_RollingRingAssemblyHarmonicAnalysis:
        """Special nested class for casting RollingRingAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
            parent: "RollingRingAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
        ) -> "RollingRingAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6942.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2794.RollingRingAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection

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
    ) -> (
        "RollingRingAssemblyHarmonicAnalysis._Cast_RollingRingAssemblyHarmonicAnalysis"
    ):
        return self._Cast_RollingRingAssemblyHarmonicAnalysis(self)

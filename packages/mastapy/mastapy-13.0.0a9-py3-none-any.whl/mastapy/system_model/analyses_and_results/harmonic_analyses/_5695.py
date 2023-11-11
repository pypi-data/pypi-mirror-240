"""BoltHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5701
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BoltHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2439
    from mastapy.system_model.analyses_and_results.static_loads import _6828
    from mastapy.system_model.analyses_and_results.system_deflections import _2707


__docformat__ = "restructuredtext en"
__all__ = ("BoltHarmonicAnalysis",)


Self = TypeVar("Self", bound="BoltHarmonicAnalysis")


class BoltHarmonicAnalysis(_5701.ComponentHarmonicAnalysis):
    """BoltHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltHarmonicAnalysis")

    class _Cast_BoltHarmonicAnalysis:
        """Special nested class for casting BoltHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
            parent: "BoltHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ):
            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis",
        ) -> "BoltHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2439.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6828.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2707.BoltSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltHarmonicAnalysis._Cast_BoltHarmonicAnalysis":
        return self._Cast_BoltHarmonicAnalysis(self)

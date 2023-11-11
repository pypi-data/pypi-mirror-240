"""CVTHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.system_deflections import _2731


__docformat__ = "restructuredtext en"
__all__ = ("CVTHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTHarmonicAnalysis")


class CVTHarmonicAnalysis(_5685.BeltDriveHarmonicAnalysis):
    """CVTHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTHarmonicAnalysis")

    class _Cast_CVTHarmonicAnalysis:
        """Special nested class for casting CVTHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
            parent: "CVTHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            return self._parent._cast(_5685.BeltDriveHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "CVTHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2731.CVTSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis":
        return self._Cast_CVTHarmonicAnalysis(self)

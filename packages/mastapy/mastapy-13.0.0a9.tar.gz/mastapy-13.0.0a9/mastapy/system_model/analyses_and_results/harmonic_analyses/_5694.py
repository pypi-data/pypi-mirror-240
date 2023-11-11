"""BoltedJointHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BoltedJointHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2440
    from mastapy.system_model.analyses_and_results.static_loads import _6827
    from mastapy.system_model.analyses_and_results.system_deflections import _2706


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointHarmonicAnalysis",)


Self = TypeVar("Self", bound="BoltedJointHarmonicAnalysis")


class BoltedJointHarmonicAnalysis(_5806.SpecialisedAssemblyHarmonicAnalysis):
    """BoltedJointHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointHarmonicAnalysis")

    class _Cast_BoltedJointHarmonicAnalysis:
        """Special nested class for casting BoltedJointHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
            parent: "BoltedJointHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
        ) -> "BoltedJointHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2440.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6827.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2706.BoltedJointSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection

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
    ) -> "BoltedJointHarmonicAnalysis._Cast_BoltedJointHarmonicAnalysis":
        return self._Cast_BoltedJointHarmonicAnalysis(self)

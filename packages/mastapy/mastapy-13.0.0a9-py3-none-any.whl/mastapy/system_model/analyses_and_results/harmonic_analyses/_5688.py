"""BevelDifferentialGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.system_model.analyses_and_results.system_deflections import _2699
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686, _5687


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetHarmonicAnalysis")


class BevelDifferentialGearSetHarmonicAnalysis(_5693.BevelGearSetHarmonicAnalysis):
    """BevelDifferentialGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearSetHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
            parent: "BevelDifferentialGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5693.BevelGearSetHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
        ) -> "BevelDifferentialGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2513.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6821.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

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
    ) -> "_2699.BevelDifferentialGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5686.BevelDifferentialGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5686.BevelDifferentialGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5687.BevelDifferentialGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5687.BevelDifferentialGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearSetHarmonicAnalysis(self)

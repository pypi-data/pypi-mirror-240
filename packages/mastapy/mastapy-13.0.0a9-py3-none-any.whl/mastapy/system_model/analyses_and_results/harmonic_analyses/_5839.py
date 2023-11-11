"""ZerolBevelGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ZerolBevelGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5837, _5838


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetHarmonicAnalysis")


class ZerolBevelGearSetHarmonicAnalysis(_5693.BevelGearSetHarmonicAnalysis):
    """ZerolBevelGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetHarmonicAnalysis")

    class _Cast_ZerolBevelGearSetHarmonicAnalysis:
        """Special nested class for casting ZerolBevelGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
            parent: "ZerolBevelGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5693.BevelGearSetHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
        ) -> "ZerolBevelGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2551.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6984.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

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
    ) -> "_2837.ZerolBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection

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
    ) -> "List[_5837.ZerolBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis]

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
    def zerol_bevel_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5837.ZerolBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5838.ZerolBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis]

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
    def zerol_bevel_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5838.ZerolBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetHarmonicAnalysis._Cast_ZerolBevelGearSetHarmonicAnalysis":
        return self._Cast_ZerolBevelGearSetHarmonicAnalysis(self)

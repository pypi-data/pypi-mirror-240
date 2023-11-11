"""KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.system_deflections import _2772
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777, _5778


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis(
    _5773.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5773.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def conical_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2538.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6917.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

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
    ) -> "_2772.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection

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
    ) -> "List[_5777.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5777.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5778.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5778.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis(
            self
        )

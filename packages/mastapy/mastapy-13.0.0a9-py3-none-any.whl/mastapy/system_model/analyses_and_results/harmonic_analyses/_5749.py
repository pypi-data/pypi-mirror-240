"""GearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.system_deflections import _2758


__docformat__ = "restructuredtext en"
__all__ = ("GearHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearHarmonicAnalysis")


class GearHarmonicAnalysis(_5782.MountableComponentHarmonicAnalysis):
    """GearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearHarmonicAnalysis")

    class _Cast_GearHarmonicAnalysis:
        """Special nested class for casting GearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
            parent: "GearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelGearHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConicalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.FaceGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelSunGearHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.ZerolBevelGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis",
        ) -> "GearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2758.GearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearHarmonicAnalysis._Cast_GearHarmonicAnalysis":
        return self._Cast_GearHarmonicAnalysis(self)

"""BevelDifferentialGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512
    from mastapy.system_model.analyses_and_results.static_loads import _6819
    from mastapy.system_model.analyses_and_results.system_deflections import _2700


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearHarmonicAnalysis")


class BevelDifferentialGearHarmonicAnalysis(_5691.BevelGearHarmonicAnalysis):
    """BevelDifferentialGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
            parent: "BevelDifferentialGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5691.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "BevelDifferentialGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2512.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6819.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2700.BevelDifferentialGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection

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
    ) -> "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearHarmonicAnalysis(self)

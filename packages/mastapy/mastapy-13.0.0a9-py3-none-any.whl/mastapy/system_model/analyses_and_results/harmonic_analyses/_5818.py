"""StraightBevelGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.system_deflections import _2815


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearHarmonicAnalysis")


class StraightBevelGearHarmonicAnalysis(_5691.BevelGearHarmonicAnalysis):
    """StraightBevelGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearHarmonicAnalysis")

    class _Cast_StraightBevelGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
            parent: "StraightBevelGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5691.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
        ) -> "StraightBevelGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6959.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

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
    ) -> "_2815.StraightBevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection

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
    ) -> "StraightBevelGearHarmonicAnalysis._Cast_StraightBevelGearHarmonicAnalysis":
        return self._Cast_StraightBevelGearHarmonicAnalysis(self)

"""StraightBevelPlanetGearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5980
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5821


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundHarmonicAnalysis")


class StraightBevelPlanetGearCompoundHarmonicAnalysis(
    _5980.StraightBevelDiffGearCompoundHarmonicAnalysis
):
    """StraightBevelPlanetGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelPlanetGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
            parent: "StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5980.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(_5891.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(
                _5879.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(_5952.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
        ) -> "StraightBevelPlanetGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5821.StraightBevelPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5821.StraightBevelPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearCompoundHarmonicAnalysis._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelPlanetGearCompoundHarmonicAnalysis(self)

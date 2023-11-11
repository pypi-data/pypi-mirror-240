"""GearCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6212,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "GearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6062,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearCompoundHarmonicAnalysisOfSingleExcitation")


class GearCompoundHarmonicAnalysisOfSingleExcitation(
    _6212.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """GearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6212.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6146,
            )

            return self._parent._cast(
                _6146.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6150,
            )

            return self._parent._cast(
                _6150.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6247,
            )

            return self._parent._cast(
                _6247.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "GearCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GearCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6062.GearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearHarmonicAnalysisOfSingleExcitation]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6062.GearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "GearCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearCompoundHarmonicAnalysisOfSingleExcitation(self)

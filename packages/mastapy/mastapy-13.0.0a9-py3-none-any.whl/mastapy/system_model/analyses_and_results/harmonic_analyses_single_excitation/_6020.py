"""BevelGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6008,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BevelGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BevelGearHarmonicAnalysisOfSingleExcitation")


class BevelGearHarmonicAnalysisOfSingleExcitation(
    _6008.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
):
    """BevelGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BevelGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
            parent: "BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6008.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(_6062.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(
                _6015.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "BevelGearHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2516.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearHarmonicAnalysisOfSingleExcitation._Cast_BevelGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelGearHarmonicAnalysisOfSingleExcitation(self)

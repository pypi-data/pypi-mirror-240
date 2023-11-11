"""AGMAGleasonConicalGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3766


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundStabilityAnalysis")


class AGMAGleasonConicalGearCompoundStabilityAnalysis(
    _3926.ConicalGearCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.HypoidGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3766.AGMAGleasonConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearStabilityAnalysis]

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
    ) -> "List[_3766.AGMAGleasonConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearStabilityAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis(self)

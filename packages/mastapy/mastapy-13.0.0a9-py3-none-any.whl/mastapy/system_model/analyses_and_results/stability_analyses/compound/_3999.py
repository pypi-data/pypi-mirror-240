"""StraightBevelDiffGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.stability_analyses import _3872


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundStabilityAnalysis")


class StraightBevelDiffGearCompoundStabilityAnalysis(
    _3910.BevelGearCompoundStabilityAnalysis
):
    """StraightBevelDiffGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
            parent: "StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
        ) -> "StraightBevelDiffGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3872.StraightBevelDiffGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearStabilityAnalysis]

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
    ) -> "List[_3872.StraightBevelDiffGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearStabilityAnalysis]

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
    ) -> "StraightBevelDiffGearCompoundStabilityAnalysis._Cast_StraightBevelDiffGearCompoundStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundStabilityAnalysis(self)

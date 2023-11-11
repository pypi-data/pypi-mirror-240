"""StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6776,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundCriticalSpeedAnalysis")


class StraightBevelPlanetGearCompoundCriticalSpeedAnalysis(
    _6776.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
):
    """StraightBevelPlanetGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelPlanetGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6776.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(_6687.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(_6729.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6653.StraightBevelPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelPlanetGearCriticalSpeedAnalysis]

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
    ) -> "List[_6653.StraightBevelPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelPlanetGearCriticalSpeedAnalysis]

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
    ) -> "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelPlanetGearCompoundCriticalSpeedAnalysis(self)

"""BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6682,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6553


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis")


class BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis(
    _6682.BevelDifferentialGearCompoundCriticalSpeedAnalysis
):
    """BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    )

    class _Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6682.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(_6687.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(_6729.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6553.BevelDifferentialPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialPlanetGearCriticalSpeedAnalysis]

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
    ) -> "List[_6553.BevelDifferentialPlanetGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelDifferentialPlanetGearCriticalSpeedAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis(self)

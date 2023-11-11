"""BevelGearSetCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6677,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundCriticalSpeedAnalysis")


class BevelGearSetCompoundCriticalSpeedAnalysis(
    _6677.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
):
    """BevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6677.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(_6705.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(
                _6769.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6671,
            )

            return self._parent._cast(
                _6671.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(
                _6684.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "BevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6557.BevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6557.BevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BevelGearSetCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundCriticalSpeedAnalysis._Cast_BevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_BevelGearSetCompoundCriticalSpeedAnalysis(self)

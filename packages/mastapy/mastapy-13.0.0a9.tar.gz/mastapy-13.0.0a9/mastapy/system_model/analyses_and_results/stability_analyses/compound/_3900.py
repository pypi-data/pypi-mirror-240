"""AGMAGleasonConicalGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3765


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundStabilityAnalysis")


class AGMAGleasonConicalGearSetCompoundStabilityAnalysis(
    _3928.ConicalGearSetCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3765.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3765.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis(self)

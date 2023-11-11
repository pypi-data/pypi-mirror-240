"""StraightBevelDiffGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.stability_analyses import _3871
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3999,
        _4000,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundStabilityAnalysis")


class StraightBevelDiffGearSetCompoundStabilityAnalysis(
    _3912.BevelGearSetCompoundStabilityAnalysis
):
    """StraightBevelDiffGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
            parent: "StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3871.StraightBevelDiffGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearSetStabilityAnalysis]

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
    def straight_bevel_diff_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_3999.StraightBevelDiffGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.StraightBevelDiffGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_4000.StraightBevelDiffGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.StraightBevelDiffGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3871.StraightBevelDiffGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearSetStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCompoundStabilityAnalysis._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundStabilityAnalysis(self)

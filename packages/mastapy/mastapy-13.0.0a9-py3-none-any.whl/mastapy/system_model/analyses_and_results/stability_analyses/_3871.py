"""StraightBevelDiffGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelDiffGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3872,
        _3870,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetStabilityAnalysis")


class StraightBevelDiffGearSetStabilityAnalysis(_3777.BevelGearSetStabilityAnalysis):
    """StraightBevelDiffGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
            parent: "StraightBevelDiffGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3777.BevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
        ) -> "StraightBevelDiffGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6958.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_stability_analysis(
        self: Self,
    ) -> "List[_3872.StraightBevelDiffGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3870.StraightBevelDiffGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelDiffGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetStabilityAnalysis._Cast_StraightBevelDiffGearSetStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearSetStabilityAnalysis(self)

"""StraightBevelDiffGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelDiffGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380, _6381


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetDynamicAnalysis")


class StraightBevelDiffGearSetDynamicAnalysis(_6291.BevelGearSetDynamicAnalysis):
    """StraightBevelDiffGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetDynamicAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
            parent: "StraightBevelDiffGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6291.BevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273

            return self._parent._cast(_6273.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
        ) -> "StraightBevelDiffGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetDynamicAnalysis.TYPE"
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
    def straight_bevel_diff_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6380.StraightBevelDiffGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6381.StraightBevelDiffGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetDynamicAnalysis._Cast_StraightBevelDiffGearSetDynamicAnalysis":
        return self._Cast_StraightBevelDiffGearSetDynamicAnalysis(self)

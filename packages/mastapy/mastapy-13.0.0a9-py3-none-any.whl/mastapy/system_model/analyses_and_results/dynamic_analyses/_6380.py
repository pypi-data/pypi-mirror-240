"""StraightBevelDiffGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelDiffGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6956


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearDynamicAnalysis")


class StraightBevelDiffGearDynamicAnalysis(_6289.BevelGearDynamicAnalysis):
    """StraightBevelDiffGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearDynamicAnalysis")

    class _Cast_StraightBevelDiffGearDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
            parent: "StraightBevelDiffGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            return self._parent._cast(_6289.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelSunGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
        ) -> "StraightBevelDiffGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearDynamicAnalysis.TYPE"
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
    def component_load_case(self: Self) -> "_6956.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearDynamicAnalysis._Cast_StraightBevelDiffGearDynamicAnalysis":
        return self._Cast_StraightBevelDiffGearDynamicAnalysis(self)

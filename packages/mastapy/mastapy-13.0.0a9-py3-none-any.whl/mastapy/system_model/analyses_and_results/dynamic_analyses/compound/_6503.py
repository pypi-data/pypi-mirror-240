"""SpiralBevelGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpiralBevelGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundDynamicAnalysis")


class SpiralBevelGearCompoundDynamicAnalysis(_6420.BevelGearCompoundDynamicAnalysis):
    """SpiralBevelGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundDynamicAnalysis"
    )

    class _Cast_SpiralBevelGearCompoundDynamicAnalysis:
        """Special nested class for casting SpiralBevelGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
            parent: "SpiralBevelGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6420.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(
                _6408.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
        ) -> "SpiralBevelGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_6374.SpiralBevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis]

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
    ) -> "List[_6374.SpiralBevelGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis]

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
    ) -> "SpiralBevelGearCompoundDynamicAnalysis._Cast_SpiralBevelGearCompoundDynamicAnalysis":
        return self._Cast_SpiralBevelGearCompoundDynamicAnalysis(self)

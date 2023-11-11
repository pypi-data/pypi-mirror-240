"""WormGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "WormGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.stability_analyses import _3890


__docformat__ = "restructuredtext en"
__all__ = ("WormGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="WormGearCompoundStabilityAnalysis")


class WormGearCompoundStabilityAnalysis(_3952.GearCompoundStabilityAnalysis):
    """WormGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearCompoundStabilityAnalysis")

    class _Cast_WormGearCompoundStabilityAnalysis:
        """Special nested class for casting WormGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
            parent: "WormGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_stability_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
        ) -> "WormGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "WormGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

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
    ) -> "List[_3890.WormGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearStabilityAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_3890.WormGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearStabilityAnalysis]

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
    ) -> "WormGearCompoundStabilityAnalysis._Cast_WormGearCompoundStabilityAnalysis":
        return self._Cast_WormGearCompoundStabilityAnalysis(self)

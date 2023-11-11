"""SynchroniserSleeveCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4009
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SynchroniserSleeveCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.stability_analyses import _3880


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundStabilityAnalysis")


class SynchroniserSleeveCompoundStabilityAnalysis(
    _4009.SynchroniserPartCompoundStabilityAnalysis
):
    """SynchroniserSleeveCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundStabilityAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundStabilityAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
            parent: "SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_4009.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "SynchroniserSleeveCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_3880.SynchroniserSleeveStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserSleeveStabilityAnalysis]

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
    ) -> "List[_3880.SynchroniserSleeveStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserSleeveStabilityAnalysis]

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
    ) -> "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis":
        return self._Cast_SynchroniserSleeveCompoundStabilityAnalysis(self)

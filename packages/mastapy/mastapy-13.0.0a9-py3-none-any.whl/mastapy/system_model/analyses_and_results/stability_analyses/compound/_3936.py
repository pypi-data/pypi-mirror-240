"""CVTPulleyCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CVTPulleyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3802


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundStabilityAnalysis")


class CVTPulleyCompoundStabilityAnalysis(_3982.PulleyCompoundStabilityAnalysis):
    """CVTPulleyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundStabilityAnalysis")

    class _Cast_CVTPulleyCompoundStabilityAnalysis:
        """Special nested class for casting CVTPulleyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
            parent: "CVTPulleyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3982.PulleyCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
        ) -> "CVTPulleyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3802.CVTPulleyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTPulleyStabilityAnalysis]

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
    ) -> "List[_3802.CVTPulleyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CVTPulleyStabilityAnalysis]

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
    ) -> "CVTPulleyCompoundStabilityAnalysis._Cast_CVTPulleyCompoundStabilityAnalysis":
        return self._Cast_CVTPulleyCompoundStabilityAnalysis(self)

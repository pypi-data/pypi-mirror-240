"""CVTPulleyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6492
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CVTPulleyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundDynamicAnalysis")


class CVTPulleyCompoundDynamicAnalysis(_6492.PulleyCompoundDynamicAnalysis):
    """CVTPulleyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundDynamicAnalysis")

    class _Cast_CVTPulleyCompoundDynamicAnalysis:
        """Special nested class for casting CVTPulleyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
            parent: "CVTPulleyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6492.PulleyCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
        ) -> "CVTPulleyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6315.CVTPulleyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6315.CVTPulleyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis]

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
    ) -> "CVTPulleyCompoundDynamicAnalysis._Cast_CVTPulleyCompoundDynamicAnalysis":
        return self._Cast_CVTPulleyCompoundDynamicAnalysis(self)

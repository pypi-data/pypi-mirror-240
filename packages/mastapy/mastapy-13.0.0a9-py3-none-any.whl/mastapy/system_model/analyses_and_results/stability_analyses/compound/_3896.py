"""AbstractShaftOrHousingCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3919
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3761


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundStabilityAnalysis")


class AbstractShaftOrHousingCompoundStabilityAnalysis(
    _3919.ComponentCompoundStabilityAnalysis
):
    """AbstractShaftOrHousingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundStabilityAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
            parent: "AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3895,
            )

            return self._parent._cast(_3895.AbstractShaftCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.FEPartCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.ShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
        ) -> "AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3761.AbstractShaftOrHousingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftOrHousingStabilityAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3761.AbstractShaftOrHousingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractShaftOrHousingStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundStabilityAnalysis._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundStabilityAnalysis(self)

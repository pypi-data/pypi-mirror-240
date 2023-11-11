"""AbstractShaftCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6673,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6540


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundCriticalSpeedAnalysis")


class AbstractShaftCompoundCriticalSpeedAnalysis(
    _6673.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
):
    """AbstractShaftCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
            parent: "AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6673.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(_6766.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "AbstractShaftCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6540.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "List[_6540.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftCompoundCriticalSpeedAnalysis(self)

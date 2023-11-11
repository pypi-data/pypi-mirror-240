"""AbstractShaftOrHousingCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5900
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5677


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundHarmonicAnalysis")


class AbstractShaftOrHousingCompoundHarmonicAnalysis(
    _5900.ComponentCompoundHarmonicAnalysis
):
    """AbstractShaftOrHousingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
            parent: "AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5900.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5876,
            )

            return self._parent._cast(_5876.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.FEPartCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.ShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
        ) -> "AbstractShaftOrHousingCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5677.AbstractShaftOrHousingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis]

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
    ) -> "List[_5677.AbstractShaftOrHousingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis]

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
    ) -> "AbstractShaftOrHousingCompoundHarmonicAnalysis._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysis(self)

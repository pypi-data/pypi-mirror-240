"""AbstractShaftCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AbstractShaftCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4569


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundModalAnalysis")


class AbstractShaftCompoundModalAnalysis(
    _4726.AbstractShaftOrHousingCompoundModalAnalysis
):
    """AbstractShaftCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftCompoundModalAnalysis")

    class _Cast_AbstractShaftCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
            parent: "AbstractShaftCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            return self._parent._cast(_4726.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CycloidalDiscCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.ShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
        ) -> "AbstractShaftCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4569.AbstractShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis]

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
    ) -> "List[_4569.AbstractShaftModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis]

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
    ) -> "AbstractShaftCompoundModalAnalysis._Cast_AbstractShaftCompoundModalAnalysis":
        return self._Cast_AbstractShaftCompoundModalAnalysis(self)

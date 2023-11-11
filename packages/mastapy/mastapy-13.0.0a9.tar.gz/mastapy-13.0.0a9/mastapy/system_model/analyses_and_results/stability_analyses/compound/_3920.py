"""ConceptCouplingCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConceptCouplingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.stability_analyses import _3788


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundStabilityAnalysis")


class ConceptCouplingCompoundStabilityAnalysis(_3931.CouplingCompoundStabilityAnalysis):
    """ConceptCouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundStabilityAnalysis"
    )

    class _Cast_ConceptCouplingCompoundStabilityAnalysis:
        """Special nested class for casting ConceptCouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
            parent: "ConceptCouplingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3931.CouplingCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
        ) -> "ConceptCouplingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2578.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2578.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3788.ConceptCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3788.ConceptCouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptCouplingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingCompoundStabilityAnalysis._Cast_ConceptCouplingCompoundStabilityAnalysis":
        return self._Cast_ConceptCouplingCompoundStabilityAnalysis(self)

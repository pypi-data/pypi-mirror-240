"""ConceptCouplingCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5280,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5141,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundModalAnalysisAtASpeed")


class ConceptCouplingCompoundModalAnalysisAtASpeed(
    _5280.CouplingCompoundModalAnalysisAtASpeed
):
    """ConceptCouplingCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ConceptCouplingCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ConceptCouplingCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
            parent: "ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5280.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5243,
            )

            return self._parent._cast(
                _5243.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
        ) -> "ConceptCouplingCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ConceptCouplingCompoundModalAnalysisAtASpeed.TYPE",
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
    ) -> "List[_5141.ConceptCouplingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptCouplingModalAnalysisAtASpeed]

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
    ) -> "List[_5141.ConceptCouplingModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConceptCouplingModalAnalysisAtASpeed]

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
    ) -> "ConceptCouplingCompoundModalAnalysisAtASpeed._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed":
        return self._Cast_ConceptCouplingCompoundModalAnalysisAtASpeed(self)

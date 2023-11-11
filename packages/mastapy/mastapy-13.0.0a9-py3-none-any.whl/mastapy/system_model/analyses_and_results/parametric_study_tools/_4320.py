"""ConceptCouplingParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConceptCouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.static_loads import _6837
    from mastapy.system_model.analyses_and_results.system_deflections import _2716


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptCouplingParametricStudyTool")


class ConceptCouplingParametricStudyTool(_4331.CouplingParametricStudyTool):
    """ConceptCouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingParametricStudyTool")

    class _Cast_ConceptCouplingParametricStudyTool:
        """Special nested class for casting ConceptCouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
            parent: "ConceptCouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            return self._parent._cast(_4331.CouplingParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4292,
            )

            return self._parent._cast(_4292.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_parametric_study_tool(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
        ) -> "ConceptCouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConceptCouplingParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6837.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2716.ConceptCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingParametricStudyTool._Cast_ConceptCouplingParametricStudyTool":
        return self._Cast_ConceptCouplingParametricStudyTool(self)

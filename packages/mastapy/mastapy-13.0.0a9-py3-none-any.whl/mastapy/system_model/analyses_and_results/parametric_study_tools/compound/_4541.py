"""SpringDamperCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4476,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpringDamperCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4414


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpringDamperCompoundParametricStudyTool")


class SpringDamperCompoundParametricStudyTool(
    _4476.CouplingCompoundParametricStudyTool
):
    """SpringDamperCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperCompoundParametricStudyTool"
    )

    class _Cast_SpringDamperCompoundParametricStudyTool:
        """Special nested class for casting SpringDamperCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
            parent: "SpringDamperCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_compound_parametric_study_tool(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4476.CouplingCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4439,
            )

            return self._parent._cast(_4439.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
        ) -> "SpringDamperCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpringDamperCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2597.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

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
    ) -> "List[_4414.SpringDamperParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperParametricStudyTool]

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
    ) -> "List[_4414.SpringDamperParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperParametricStudyTool]

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
    ) -> "SpringDamperCompoundParametricStudyTool._Cast_SpringDamperCompoundParametricStudyTool":
        return self._Cast_SpringDamperCompoundParametricStudyTool(self)

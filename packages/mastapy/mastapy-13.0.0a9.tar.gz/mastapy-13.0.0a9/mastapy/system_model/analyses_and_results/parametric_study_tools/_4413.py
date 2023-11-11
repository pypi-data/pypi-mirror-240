"""SpringDamperHalfParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpringDamperHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2808


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfParametricStudyTool",)


Self = TypeVar("Self", bound="SpringDamperHalfParametricStudyTool")


class SpringDamperHalfParametricStudyTool(_4330.CouplingHalfParametricStudyTool):
    """SpringDamperHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfParametricStudyTool")

    class _Cast_SpringDamperHalfParametricStudyTool:
        """Special nested class for casting SpringDamperHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
            parent: "SpringDamperHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            return self._parent._cast(_4330.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
        ) -> "SpringDamperHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpringDamperHalfParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6954.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2808.SpringDamperHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpringDamperHalfParametricStudyTool._Cast_SpringDamperHalfParametricStudyTool"
    ):
        return self._Cast_SpringDamperHalfParametricStudyTool(self)

"""CouplingParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingParametricStudyTool")


class CouplingParametricStudyTool(_4408.SpecialisedAssemblyParametricStudyTool):
    """CouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingParametricStudyTool")

    class _Cast_CouplingParametricStudyTool:
        """Special nested class for casting CouplingParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            parent: "CouplingParametricStudyTool",
        ):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            return self._parent._cast(_4408.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4292,
            )

            return self._parent._cast(_4292.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ConceptCouplingParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartToPartShearCouplingParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpringDamperParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.TorqueConverterParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
        ) -> "CouplingParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingParametricStudyTool._Cast_CouplingParametricStudyTool":
        return self._Cast_CouplingParametricStudyTool(self)

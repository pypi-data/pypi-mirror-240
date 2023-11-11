"""PlanetaryGearSetCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4488,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PlanetaryGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4394


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundParametricStudyTool")


class PlanetaryGearSetCompoundParametricStudyTool(
    _4488.CylindricalGearSetCompoundParametricStudyTool
):
    """PlanetaryGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundParametricStudyTool"
    )

    class _Cast_PlanetaryGearSetCompoundParametricStudyTool:
        """Special nested class for casting PlanetaryGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
            parent: "PlanetaryGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4488.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4439,
            )

            return self._parent._cast(_4439.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
        ) -> "PlanetaryGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4394.PlanetaryGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool]

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
    ) -> "List[_4394.PlanetaryGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PlanetaryGearSetParametricStudyTool]

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
    ) -> "PlanetaryGearSetCompoundParametricStudyTool._Cast_PlanetaryGearSetCompoundParametricStudyTool":
        return self._Cast_PlanetaryGearSetCompoundParametricStudyTool(self)

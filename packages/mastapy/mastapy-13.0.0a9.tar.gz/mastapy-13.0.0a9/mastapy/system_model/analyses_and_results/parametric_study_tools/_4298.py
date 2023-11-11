"""AGMAGleasonConicalGearSetParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4326
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetParametricStudyTool")


class AGMAGleasonConicalGearSetParametricStudyTool(
    _4326.ConicalGearSetParametricStudyTool
):
    """AGMAGleasonConicalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearSetParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
            parent: "AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            return self._parent._cast(_4326.ConicalGearSetParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4292,
            )

            return self._parent._cast(_4292.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.HypoidGearSetParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.ZerolBevelGearSetParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
        ) -> "AGMAGleasonConicalGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetParametricStudyTool._Cast_AGMAGleasonConicalGearSetParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearSetParametricStudyTool(self)

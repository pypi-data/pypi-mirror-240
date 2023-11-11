"""BevelGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BevelGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearParametricStudyTool",)


Self = TypeVar("Self", bound="BevelGearParametricStudyTool")


class BevelGearParametricStudyTool(_4297.AGMAGleasonConicalGearParametricStudyTool):
    """BevelGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearParametricStudyTool")

    class _Cast_BevelGearParametricStudyTool:
        """Special nested class for casting BevelGearParametricStudyTool to subclasses."""

        def __init__(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
            parent: "BevelGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            return self._parent._cast(_4297.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(
                _4306.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialSunGearParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelSunGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
        ) -> "BevelGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2516.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearParametricStudyTool._Cast_BevelGearParametricStudyTool":
        return self._Cast_BevelGearParametricStudyTool(self)

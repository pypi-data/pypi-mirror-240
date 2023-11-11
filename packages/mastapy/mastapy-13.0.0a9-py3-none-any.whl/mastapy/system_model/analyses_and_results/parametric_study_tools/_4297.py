"""AGMAGleasonConicalGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4325
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AGMAGleasonConicalGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearParametricStudyTool")


class AGMAGleasonConicalGearParametricStudyTool(_4325.ConicalGearParametricStudyTool):
    """AGMAGleasonConicalGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
            parent: "AGMAGleasonConicalGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            return self._parent._cast(_4325.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(
                _4306.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelGearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.HypoidGearParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelSunGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
        ) -> "AGMAGleasonConicalGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2510.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearParametricStudyTool._Cast_AGMAGleasonConicalGearParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearParametricStudyTool(self)

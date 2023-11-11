"""AGMAGleasonConicalGearCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4471,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundParametricStudyTool")


class AGMAGleasonConicalGearCompoundParametricStudyTool(
    _4471.ConicalGearCompoundParametricStudyTool
):
    """AGMAGleasonConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundParametricStudyTool"
    )

    class _Cast_AGMAGleasonConicalGearCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
            parent: "AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4471.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(
                _4450.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BevelGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.HypoidGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
        ) -> "AGMAGleasonConicalGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4297.AGMAGleasonConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4297.AGMAGleasonConicalGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AGMAGleasonConicalGearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool":
        return self._Cast_AGMAGleasonConicalGearCompoundParametricStudyTool(self)

"""ZerolBevelGearParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ZerolBevelGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.system_deflections import _2838


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearParametricStudyTool")


class ZerolBevelGearParametricStudyTool(_4309.BevelGearParametricStudyTool):
    """ZerolBevelGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearParametricStudyTool")

    class _Cast_ZerolBevelGearParametricStudyTool:
        """Special nested class for casting ZerolBevelGearParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
            parent: "ZerolBevelGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            return self._parent._cast(_4309.BevelGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
        ) -> "ZerolBevelGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool",
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
        self: Self, instance_to_wrap: "ZerolBevelGearParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6982.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "List[_2838.ZerolBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection]

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
    ) -> "ZerolBevelGearParametricStudyTool._Cast_ZerolBevelGearParametricStudyTool":
        return self._Cast_ZerolBevelGearParametricStudyTool(self)

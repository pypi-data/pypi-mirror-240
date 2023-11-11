"""RingPinsCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4516,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "RingPinsCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="RingPinsCompoundParametricStudyTool")


class RingPinsCompoundParametricStudyTool(
    _4516.MountableComponentCompoundParametricStudyTool
):
    """RingPinsCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsCompoundParametricStudyTool")

    class _Cast_RingPinsCompoundParametricStudyTool:
        """Special nested class for casting RingPinsCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
            parent: "RingPinsCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4516.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
        ) -> "RingPinsCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "RingPinsCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4399.RingPinsParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RingPinsParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4399.RingPinsParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.RingPinsParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> (
        "RingPinsCompoundParametricStudyTool._Cast_RingPinsCompoundParametricStudyTool"
    ):
        return self._Cast_RingPinsCompoundParametricStudyTool(self)

"""StraightBevelDiffGearMeshParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "StraightBevelDiffGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2810


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshParametricStudyTool")


class StraightBevelDiffGearMeshParametricStudyTool(
    _4308.BevelGearMeshParametricStudyTool
):
    """StraightBevelDiffGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshParametricStudyTool"
    )

    class _Cast_StraightBevelDiffGearMeshParametricStudyTool:
        """Special nested class for casting StraightBevelDiffGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
            parent: "StraightBevelDiffGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            return self._parent._cast(_4308.BevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(
                _4296.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(
                _4364.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
        ) -> "StraightBevelDiffGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool",
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
        instance_to_wrap: "StraightBevelDiffGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2810.StraightBevelDiffGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshParametricStudyTool._Cast_StraightBevelDiffGearMeshParametricStudyTool":
        return self._Cast_StraightBevelDiffGearMeshParametricStudyTool(self)

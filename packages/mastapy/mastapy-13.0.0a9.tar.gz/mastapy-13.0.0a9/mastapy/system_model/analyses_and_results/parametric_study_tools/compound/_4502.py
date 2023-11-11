"""HypoidGearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4444,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "HypoidGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4361


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundParametricStudyTool")


class HypoidGearMeshCompoundParametricStudyTool(
    _4444.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
):
    """HypoidGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundParametricStudyTool"
    )

    class _Cast_HypoidGearMeshCompoundParametricStudyTool:
        """Special nested class for casting HypoidGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
            parent: "HypoidGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4444.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(
                _4504.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
        ) -> "HypoidGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "HypoidGearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4361.HypoidGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4361.HypoidGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.HypoidGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearMeshCompoundParametricStudyTool._Cast_HypoidGearMeshCompoundParametricStudyTool":
        return self._Cast_HypoidGearMeshCompoundParametricStudyTool(self)

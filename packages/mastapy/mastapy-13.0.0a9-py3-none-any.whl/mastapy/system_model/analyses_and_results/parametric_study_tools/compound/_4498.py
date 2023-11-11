"""GearMeshCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4357


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GearMeshCompoundParametricStudyTool")


class GearMeshCompoundParametricStudyTool(
    _4504.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """GearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundParametricStudyTool")

    class _Cast_GearMeshCompoundParametricStudyTool:
        """Special nested class for casting GearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
            parent: "GearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            return self._parent._cast(
                _4504.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4444,
            )

            return self._parent._cast(
                _4444.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(_4456.BevelGearMeshCompoundParametricStudyTool)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(
                _4487.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(_4493.FaceGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(
                _4506.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(
                _4539.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(
                _4545.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(_4563.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(
                _4566.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "GearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "GearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4357.GearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4357.GearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> (
        "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool"
    ):
        return self._Cast_GearMeshCompoundParametricStudyTool(self)

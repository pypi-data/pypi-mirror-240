"""StraightBevelGearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5260,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2324
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5222,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundModalAnalysisAtASpeed")


class StraightBevelGearMeshCompoundModalAnalysisAtASpeed(
    _5260.BevelGearMeshCompoundModalAnalysisAtASpeed
):
    """StraightBevelGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelGearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
            parent: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5260.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5248,
            )

            return self._parent._cast(
                _5248.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(
                _5276.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(
                _5308.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
        ) -> "StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2324.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2324.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

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
    ) -> "List[_5222.StraightBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelGearMeshModalAnalysisAtASpeed]

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
    ) -> "List[_5222.StraightBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelGearMeshModalAnalysisAtASpeed]

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
    ) -> "StraightBevelGearMeshCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_StraightBevelGearMeshCompoundModalAnalysisAtASpeed(self)

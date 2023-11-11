"""WormGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5171
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.static_loads import _6980


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearMeshModalAnalysisAtASpeed")


class WormGearMeshModalAnalysisAtASpeed(_5171.GearMeshModalAnalysisAtASpeed):
    """WormGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshModalAnalysisAtASpeed")

    class _Cast_WormGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting WormGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
            parent: "WormGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5171.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(
                _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
        ) -> "WormGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "WormGearMeshModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2326.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6980.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshModalAnalysisAtASpeed._Cast_WormGearMeshModalAnalysisAtASpeed":
        return self._Cast_WormGearMeshModalAnalysisAtASpeed(self)

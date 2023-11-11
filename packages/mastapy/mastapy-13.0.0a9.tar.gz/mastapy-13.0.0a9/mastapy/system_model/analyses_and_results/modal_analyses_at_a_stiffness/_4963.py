"""StraightBevelGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4869,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2324
    from mastapy.system_model.analyses_and_results.static_loads import _6960


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelGearMeshModalAnalysisAtAStiffness")


class StraightBevelGearMeshModalAnalysisAtAStiffness(
    _4869.BevelGearMeshModalAnalysisAtAStiffness
):
    """StraightBevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
            parent: "StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4869.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(
                _4857.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(_4885.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(_4912.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(
                _4919.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
        ) -> "StraightBevelGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelGearMeshModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6960.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

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
    ) -> "StraightBevelGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelGearMeshModalAnalysisAtAStiffness(self)

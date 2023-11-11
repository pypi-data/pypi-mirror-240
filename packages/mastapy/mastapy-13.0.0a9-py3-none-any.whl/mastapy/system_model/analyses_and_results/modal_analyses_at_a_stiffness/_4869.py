"""BevelGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4857,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2300


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtAStiffness")


class BevelGearMeshModalAnalysisAtAStiffness(
    _4857.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
):
    """BevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
            parent: "BevelGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4857.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(_4885.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(_4912.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(
                _4919.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4864,
            )

            return self._parent._cast(
                _4864.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(
                _4960.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(_4981.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "BevelGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2300.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness":
        return self._Cast_BevelGearMeshModalAnalysisAtAStiffness(self)

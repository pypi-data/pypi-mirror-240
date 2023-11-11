"""GearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearMeshModalAnalysisAtASpeed")


class GearMeshModalAnalysisAtASpeed(
    _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """GearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshModalAnalysisAtASpeed")

    class _Cast_GearMeshModalAnalysisAtASpeed:
        """Special nested class for casting GearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
            parent: "GearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(
                _5117.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(
                _5124.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(_5129.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(
                _5219.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(_5222.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
        ) -> "GearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2310.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

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
    ) -> "GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed":
        return self._Cast_GearMeshModalAnalysisAtASpeed(self)

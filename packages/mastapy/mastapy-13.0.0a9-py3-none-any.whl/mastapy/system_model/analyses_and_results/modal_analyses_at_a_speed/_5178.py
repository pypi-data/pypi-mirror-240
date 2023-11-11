"""InterMountableComponentConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5148
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionModalAnalysisAtASpeed")


class InterMountableComponentConnectionModalAnalysisAtASpeed(
    _5148.ConnectionModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionModalAnalysisAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
            parent: "InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(
                _5117.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(_5122.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(
                _5124.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(_5129.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5134,
            )

            return self._parent._cast(_5134.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(
                _5139.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5182,
            )

            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(
                _5194.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(
                _5204.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(
                _5219.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(_5222.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(
                _5231.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
        ) -> "InterMountableComponentConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2278.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "InterMountableComponentConnectionModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed":
        return self._Cast_InterMountableComponentConnectionModalAnalysisAtASpeed(self)

"""InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3277,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
)


class InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
    _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
):
    """InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.BeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.ClutchConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3271,
            )

            return self._parent._cast(
                _3271.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.CouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3289,
            )

            return self._parent._cast(
                _3289.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.FaceGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3314,
            )

            return self._parent._cast(
                _3314.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3334,
            )

            return self._parent._cast(
                _3334.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3344,
            )

            return self._parent._cast(
                _3344.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(
                _3348.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.WormGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )

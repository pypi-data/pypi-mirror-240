"""GearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3046,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "GearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GearMeshSteadyStateSynchronousResponse")


class GearMeshSteadyStateSynchronousResponse(
    _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """GearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_GearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting GearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
            parent: "GearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(_2996.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3009,
            )

            return self._parent._cast(
                _3009.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3027,
            )

            return self._parent._cast(
                _3027.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(_3034.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(
                _3043.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(
                _3050.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(
                _3080.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(_3107.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
        ) -> "GearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "GearMeshSteadyStateSynchronousResponse.TYPE"
    ):
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
    ) -> "GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse":
        return self._Cast_GearMeshSteadyStateSynchronousResponse(self)

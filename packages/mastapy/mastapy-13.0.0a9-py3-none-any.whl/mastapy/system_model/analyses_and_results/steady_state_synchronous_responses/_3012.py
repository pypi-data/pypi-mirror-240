"""ConicalGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3039,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConicalGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2304


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearMeshSteadyStateSynchronousResponse")


class ConicalGearMeshSteadyStateSynchronousResponse(
    _3039.GearMeshSteadyStateSynchronousResponse
):
    """ConicalGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
            parent: "ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3039.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(
                _2991.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(_2996.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(
                _3043.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3050,
            )

            return self._parent._cast(
                _3050.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3053,
            )

            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(
                _3080.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3092,
            )

            return self._parent._cast(
                _3092.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3110,
            )

            return self._parent._cast(
                _3110.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
        ) -> "ConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConicalGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2304.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshSteadyStateSynchronousResponse._Cast_ConicalGearMeshSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearMeshSteadyStateSynchronousResponse(self)

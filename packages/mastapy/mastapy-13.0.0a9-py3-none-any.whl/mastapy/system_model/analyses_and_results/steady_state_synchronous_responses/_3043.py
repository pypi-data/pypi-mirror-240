"""HypoidGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2984,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "HypoidGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6903


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="HypoidGearMeshSteadyStateSynchronousResponse")


class HypoidGearMeshSteadyStateSynchronousResponse(
    _2984.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
):
    """HypoidGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_HypoidGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
            parent: "HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2984.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "HypoidGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "HypoidGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6903.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse":
        return self._Cast_HypoidGearMeshSteadyStateSynchronousResponse(self)

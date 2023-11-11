"""KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3047,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.static_loads import _6913


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse"
)


class KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse(
    _3047.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3047.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(
                _3046.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2316.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse(
            self
        )

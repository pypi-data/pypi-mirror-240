"""AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3274,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3274.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3274.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(
                _3348.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3351,
            )

            return self._parent._cast(
                _3351.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3369,
            )

            return self._parent._cast(
                _3369.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2296.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )

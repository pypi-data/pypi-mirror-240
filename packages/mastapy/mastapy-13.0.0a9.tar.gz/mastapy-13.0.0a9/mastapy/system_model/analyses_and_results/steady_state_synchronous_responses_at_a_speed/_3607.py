"""StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3517,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3517.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3517.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3505,
            )

            return self._parent._cast(
                _3505.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

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
    ) -> "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )

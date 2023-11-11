"""StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3258,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft"
)


class StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3258.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3258.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3274,
            )

            return self._parent._cast(
                _3274.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )

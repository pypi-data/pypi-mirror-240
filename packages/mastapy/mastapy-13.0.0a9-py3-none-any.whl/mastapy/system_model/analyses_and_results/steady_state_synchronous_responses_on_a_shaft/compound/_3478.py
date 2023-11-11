"""StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3389,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3348,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)


class StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3389.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3389.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3377,
            )

            return self._parent._cast(
                _3377.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3407,
            )

            return self._parent._cast(
                _3407.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3348.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3348.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )

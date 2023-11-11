"""CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3559,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2306
    from mastapy.system_model.analyses_and_results.static_loads import _6860


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"
)


class CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3559.GearMeshSteadyStateSynchronousResponseAtASpeed
):
    """CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3559.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2306.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6860.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed(
            self
        )

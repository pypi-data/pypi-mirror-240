"""CouplingConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3566,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CouplingConnectionSteadyStateSynchronousResponseAtASpeed")


class CouplingConnectionSteadyStateSynchronousResponseAtASpeed(
    _3566.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """CouplingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3566.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CouplingConnectionSteadyStateSynchronousResponseAtASpeed(self)

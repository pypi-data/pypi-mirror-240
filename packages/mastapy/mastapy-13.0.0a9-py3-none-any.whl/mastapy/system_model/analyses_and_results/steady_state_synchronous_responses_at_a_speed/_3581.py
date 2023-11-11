"""PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3538,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6926


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
)


class PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed(
    _3538.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
):
    """PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3538.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(
                _3566.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2345.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "_6926.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

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
    ) -> "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )

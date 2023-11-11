"""RollingRingConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RollingRingConnectionModalAnalysisAtASpeed")


class RollingRingConnectionModalAnalysisAtASpeed(
    _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """RollingRingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionModalAnalysisAtASpeed"
    )

    class _Cast_RollingRingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting RollingRingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
            parent: "RollingRingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
        ) -> "RollingRingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "RollingRingConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2289.RollingRingConnection":
        """mastapy.system_model.connections_and_sockets.RollingRingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6943.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.RollingRingConnectionModalAnalysisAtASpeed]

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
    ) -> "RollingRingConnectionModalAnalysisAtASpeed._Cast_RollingRingConnectionModalAnalysisAtASpeed":
        return self._Cast_RollingRingConnectionModalAnalysisAtASpeed(self)

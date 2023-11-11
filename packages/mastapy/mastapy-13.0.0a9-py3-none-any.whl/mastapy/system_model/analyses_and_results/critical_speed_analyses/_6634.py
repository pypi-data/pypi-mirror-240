"""RollingRingConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RollingRingConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RollingRingConnectionCriticalSpeedAnalysis")


class RollingRingConnectionCriticalSpeedAnalysis(
    _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """RollingRingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingConnectionCriticalSpeedAnalysis"
    )

    class _Cast_RollingRingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting RollingRingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
            parent: "RollingRingConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
        ) -> "RollingRingConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingConnectionCriticalSpeedAnalysis.TYPE"
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
    def planetaries(self: Self) -> "List[RollingRingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RollingRingConnectionCriticalSpeedAnalysis]

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
    ) -> "RollingRingConnectionCriticalSpeedAnalysis._Cast_RollingRingConnectionCriticalSpeedAnalysis":
        return self._Cast_RollingRingConnectionCriticalSpeedAnalysis(self)

"""BeltConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BeltConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2265
    from mastapy.system_model.analyses_and_results.static_loads import _6817


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCriticalSpeedAnalysis")


class BeltConnectionCriticalSpeedAnalysis(
    _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """BeltConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionCriticalSpeedAnalysis")

    class _Cast_BeltConnectionCriticalSpeedAnalysis:
        """Special nested class for casting BeltConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
            parent: "BeltConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
        ) -> "BeltConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2265.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6817.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

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
    ) -> (
        "BeltConnectionCriticalSpeedAnalysis._Cast_BeltConnectionCriticalSpeedAnalysis"
    ):
        return self._Cast_BeltConnectionCriticalSpeedAnalysis(self)

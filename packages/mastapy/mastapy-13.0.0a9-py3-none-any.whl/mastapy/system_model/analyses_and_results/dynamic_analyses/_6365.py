"""RingPinsToDiscConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "RingPinsToDiscConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6941


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionDynamicAnalysis")


class RingPinsToDiscConnectionDynamicAnalysis(
    _6340.InterMountableComponentConnectionDynamicAnalysis
):
    """RingPinsToDiscConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionDynamicAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionDynamicAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
            parent: "RingPinsToDiscConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            return self._parent._cast(
                _6340.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_dynamic_analysis(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
        ) -> "RingPinsToDiscConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2338.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6941.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "RingPinsToDiscConnectionDynamicAnalysis._Cast_RingPinsToDiscConnectionDynamicAnalysis":
        return self._Cast_RingPinsToDiscConnectionDynamicAnalysis(self)

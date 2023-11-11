"""CoaxialConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CoaxialConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.static_loads import _6833


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionStabilityAnalysis")


class CoaxialConnectionStabilityAnalysis(
    _3859.ShaftToMountableComponentConnectionStabilityAnalysis
):
    """CoaxialConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionStabilityAnalysis")

    class _Cast_CoaxialConnectionStabilityAnalysis:
        """Special nested class for casting CoaxialConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
            parent: "CoaxialConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            return self._parent._cast(
                _3859.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(
                _3763.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(
                _3805.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def coaxial_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ) -> "CoaxialConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6833.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

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
    ) -> "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis":
        return self._Cast_CoaxialConnectionStabilityAnalysis(self)

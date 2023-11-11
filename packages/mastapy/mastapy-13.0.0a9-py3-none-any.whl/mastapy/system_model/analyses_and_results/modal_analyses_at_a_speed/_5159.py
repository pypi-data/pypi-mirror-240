"""CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6857


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"
)


class CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed(
    _5116.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
):
    """CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
            parent: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5116.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
        ) -> "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2335.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "_6857.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed(
            self
        )

"""CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2332


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"
)


class CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed(
    _5137.CoaxialConnectionModalAnalysisAtASpeed
):
    """CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
            parent: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5137.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(
                _5211.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5116,
            )

            return self._parent._cast(
                _5116.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
        ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2332.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed(
            self
        )

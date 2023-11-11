"""ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5246,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5211,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
)


class ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5246.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5246.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(
                _5267.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(
                _5287.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(
                _5326.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5211.ShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ShaftToMountableComponentConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5211.ShaftToMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ShaftToMountableComponentConnectionModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return (
            self._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed(
                self
            )
        )

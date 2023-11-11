"""ShaftHubConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.static_loads import _6946


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ShaftHubConnectionModalAnalysisAtASpeed")


class ShaftHubConnectionModalAnalysisAtASpeed(_5149.ConnectorModalAnalysisAtASpeed):
    """ShaftHubConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionModalAnalysisAtASpeed"
    )

    class _Cast_ShaftHubConnectionModalAnalysisAtASpeed:
        """Special nested class for casting ShaftHubConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
            parent: "ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connector_modal_analysis_at_a_speed(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5149.ConnectorModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
        ) -> "ShaftHubConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6946.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ShaftHubConnectionModalAnalysisAtASpeed]

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
    ) -> "ShaftHubConnectionModalAnalysisAtASpeed._Cast_ShaftHubConnectionModalAnalysisAtASpeed":
        return self._Cast_ShaftHubConnectionModalAnalysisAtASpeed(self)

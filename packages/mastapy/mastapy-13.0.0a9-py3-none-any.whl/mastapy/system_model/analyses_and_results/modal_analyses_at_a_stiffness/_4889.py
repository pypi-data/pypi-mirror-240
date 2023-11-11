"""ConnectorModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4932,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConnectorModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConnectorModalAnalysisAtAStiffness")


class ConnectorModalAnalysisAtAStiffness(
    _4932.MountableComponentModalAnalysisAtAStiffness
):
    """ConnectorModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysisAtAStiffness")

    class _Cast_ConnectorModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectorModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
            parent: "ConnectorModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4861,
            )

            return self._parent._cast(_4861.BearingModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.OilSealModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(_4950.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
        ) -> "ConnectorModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConnectorModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2444.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorModalAnalysisAtAStiffness._Cast_ConnectorModalAnalysisAtAStiffness":
        return self._Cast_ConnectorModalAnalysisAtAStiffness(self)

"""SpringDamperConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4890,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SpringDamperConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _6953


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpringDamperConnectionModalAnalysisAtAStiffness")


class SpringDamperConnectionModalAnalysisAtAStiffness(
    _4890.CouplingConnectionModalAnalysisAtAStiffness
):
    """SpringDamperConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionModalAnalysisAtAStiffness"
    )

    class _Cast_SpringDamperConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting SpringDamperConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
            parent: "SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4890.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(
                _4919.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
        ) -> "SpringDamperConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpringDamperConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6953.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionModalAnalysisAtAStiffness._Cast_SpringDamperConnectionModalAnalysisAtAStiffness":
        return self._Cast_SpringDamperConnectionModalAnalysisAtAStiffness(self)

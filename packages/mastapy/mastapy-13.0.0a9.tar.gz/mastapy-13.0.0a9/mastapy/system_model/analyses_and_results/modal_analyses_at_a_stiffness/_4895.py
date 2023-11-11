"""CVTPulleyModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4943,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTPulleyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTPulleyModalAnalysisAtAStiffness")


class CVTPulleyModalAnalysisAtAStiffness(_4943.PulleyModalAnalysisAtAStiffness):
    """CVTPulleyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyModalAnalysisAtAStiffness")

    class _Cast_CVTPulleyModalAnalysisAtAStiffness:
        """Special nested class for casting CVTPulleyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
            parent: "CVTPulleyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4943.PulleyModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "CVTPulleyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CVTPulleyModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2584.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

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
    ) -> "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness":
        return self._Cast_CVTPulleyModalAnalysisAtAStiffness(self)

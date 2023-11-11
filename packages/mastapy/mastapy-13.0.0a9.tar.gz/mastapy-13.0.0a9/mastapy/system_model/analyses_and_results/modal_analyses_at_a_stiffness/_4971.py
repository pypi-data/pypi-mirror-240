"""SynchroniserSleeveModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4970,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SynchroniserSleeveModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.static_loads import _6967


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserSleeveModalAnalysisAtAStiffness")


class SynchroniserSleeveModalAnalysisAtAStiffness(
    _4970.SynchroniserPartModalAnalysisAtAStiffness
):
    """SynchroniserSleeveModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserSleeveModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserSleeveModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
            parent: "SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4970.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
        ) -> "SynchroniserSleeveModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6967.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveModalAnalysisAtAStiffness._Cast_SynchroniserSleeveModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserSleeveModalAnalysisAtAStiffness(self)

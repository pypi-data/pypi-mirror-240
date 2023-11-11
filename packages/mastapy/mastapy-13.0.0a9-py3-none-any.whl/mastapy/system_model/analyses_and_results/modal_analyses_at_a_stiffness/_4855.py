"""AbstractShaftOrHousingModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4878,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftOrHousingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysisAtAStiffness")


class AbstractShaftOrHousingModalAnalysisAtAStiffness(
    _4878.ComponentModalAnalysisAtAStiffness
):
    """AbstractShaftOrHousingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
            parent: "AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4854,
            )

            return self._parent._cast(_4854.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(_4898.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.FEPartModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(_4951.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftOrHousingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness(self)

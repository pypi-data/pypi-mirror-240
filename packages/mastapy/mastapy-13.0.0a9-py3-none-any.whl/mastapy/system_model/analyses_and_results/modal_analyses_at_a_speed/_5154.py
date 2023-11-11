"""CVTModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CVTModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583


__docformat__ = "restructuredtext en"
__all__ = ("CVTModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CVTModalAnalysisAtASpeed")


class CVTModalAnalysisAtASpeed(_5123.BeltDriveModalAnalysisAtASpeed):
    """CVTModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CVT_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTModalAnalysisAtASpeed")

    class _Cast_CVTModalAnalysisAtASpeed:
        """Special nested class for casting CVTModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
            parent: "CVTModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5123.BeltDriveModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5113,
            )

            return self._parent._cast(_5113.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed",
        ) -> "CVTModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTModalAnalysisAtASpeed._Cast_CVTModalAnalysisAtASpeed":
        return self._Cast_CVTModalAnalysisAtASpeed(self)

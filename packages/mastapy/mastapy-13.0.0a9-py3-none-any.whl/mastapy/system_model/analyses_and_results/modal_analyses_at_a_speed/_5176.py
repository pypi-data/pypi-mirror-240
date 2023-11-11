"""HypoidGearModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.static_loads import _6902


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="HypoidGearModalAnalysisAtASpeed")


class HypoidGearModalAnalysisAtASpeed(
    _5118.AGMAGleasonConicalGearModalAnalysisAtASpeed
):
    """HypoidGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearModalAnalysisAtASpeed")

    class _Cast_HypoidGearModalAnalysisAtASpeed:
        """Special nested class for casting HypoidGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
            parent: "HypoidGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5118.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
        ) -> "HypoidGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6902.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

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
    ) -> "HypoidGearModalAnalysisAtASpeed._Cast_HypoidGearModalAnalysisAtASpeed":
        return self._Cast_HypoidGearModalAnalysisAtASpeed(self)

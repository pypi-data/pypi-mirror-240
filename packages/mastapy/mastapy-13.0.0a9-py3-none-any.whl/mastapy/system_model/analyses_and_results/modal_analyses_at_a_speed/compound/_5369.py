"""ZerolBevelGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5259,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5241,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ZerolBevelGearCompoundModalAnalysisAtASpeed")


class ZerolBevelGearCompoundModalAnalysisAtASpeed(
    _5259.BevelGearCompoundModalAnalysisAtASpeed
):
    """ZerolBevelGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ZerolBevelGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
            parent: "ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5259.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
        ) -> "ZerolBevelGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ZerolBevelGearCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5241.ZerolBevelGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5241.ZerolBevelGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed":
        return self._Cast_ZerolBevelGearCompoundModalAnalysisAtASpeed(self)

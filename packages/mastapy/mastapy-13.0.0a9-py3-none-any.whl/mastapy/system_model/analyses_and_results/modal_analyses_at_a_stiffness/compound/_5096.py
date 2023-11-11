"""StraightBevelSunGearCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5089,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4967,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundModalAnalysisAtAStiffness")


class StraightBevelSunGearCompoundModalAnalysisAtAStiffness(
    _5089.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
):
    """StraightBevelSunGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelSunGearCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
            parent: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5089.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(_5000.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(_5042.GearCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(_5009.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
        ) -> "StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelSunGearCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4967.StraightBevelSunGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelSunGearModalAnalysisAtAStiffness]

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
    ) -> "List[_4967.StraightBevelSunGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelSunGearModalAnalysisAtAStiffness]

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
    ) -> "StraightBevelSunGearCompoundModalAnalysisAtAStiffness._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelSunGearCompoundModalAnalysisAtAStiffness(self)

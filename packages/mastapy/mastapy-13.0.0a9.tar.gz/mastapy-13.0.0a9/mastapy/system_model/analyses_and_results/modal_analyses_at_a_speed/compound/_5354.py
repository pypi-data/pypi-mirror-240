"""StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5348,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5225,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundModalAnalysisAtASpeed")


class StraightBevelPlanetGearCompoundModalAnalysisAtASpeed(
    _5348.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
):
    """StraightBevelPlanetGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelPlanetGearCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
            parent: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5348.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(_5259.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.GearCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
        ) -> "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5225.StraightBevelPlanetGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelPlanetGearModalAnalysisAtASpeed]

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
    ) -> "List[_5225.StraightBevelPlanetGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelPlanetGearModalAnalysisAtASpeed]

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
    ) -> "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
        return self._Cast_StraightBevelPlanetGearCompoundModalAnalysisAtASpeed(self)

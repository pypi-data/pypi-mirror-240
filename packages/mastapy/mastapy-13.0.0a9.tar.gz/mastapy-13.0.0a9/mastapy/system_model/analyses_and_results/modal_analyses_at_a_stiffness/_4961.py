"""StraightBevelDiffGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelDiffGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6956


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelDiffGearModalAnalysisAtAStiffness")


class StraightBevelDiffGearModalAnalysisAtAStiffness(
    _4870.BevelGearModalAnalysisAtAStiffness
):
    """StraightBevelDiffGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelDiffGearModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
            parent: "StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4870.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ) -> "StraightBevelDiffGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelDiffGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6956.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness(self)

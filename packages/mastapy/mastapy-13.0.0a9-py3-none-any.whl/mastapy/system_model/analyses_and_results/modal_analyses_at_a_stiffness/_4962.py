"""StraightBevelDiffGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4871,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelDiffGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4961,
        _4960,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetModalAnalysisAtAStiffness")


class StraightBevelDiffGearSetModalAnalysisAtAStiffness(
    _4871.BevelGearSetModalAnalysisAtAStiffness
):
    """StraightBevelDiffGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
            parent: "StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4871.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4853,
            )

            return self._parent._cast(_4853.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
        ) -> "StraightBevelDiffGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelDiffGearSetModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4961.StraightBevelDiffGearModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelDiffGearModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis_at_a_stiffness(
        self: Self,
    ) -> "List[_4960.StraightBevelDiffGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.StraightBevelDiffGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysisAtAStiffness

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelDiffGearSetModalAnalysisAtAStiffness(self)

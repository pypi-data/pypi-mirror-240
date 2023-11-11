"""SpiralBevelGearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5261,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5215,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5342,
        _5343,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundModalAnalysisAtASpeed")


class SpiralBevelGearSetCompoundModalAnalysisAtASpeed(
    _5261.BevelGearSetCompoundModalAnalysisAtASpeed
):
    """SpiralBevelGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpiralBevelGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
            parent: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5261.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5243,
            )

            return self._parent._cast(
                _5243.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2541.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5215.SpiralBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpiralBevelGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5342.SpiralBevelGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.SpiralBevelGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5343.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5215.SpiralBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpiralBevelGearSetModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetCompoundModalAnalysisAtASpeed._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_SpiralBevelGearSetCompoundModalAnalysisAtASpeed(self)

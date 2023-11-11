"""GearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5341,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "GearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5173,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearSetCompoundModalAnalysisAtASpeed")


class GearSetCompoundModalAnalysisAtASpeed(
    _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
):
    """GearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundModalAnalysisAtASpeed")

    class _Cast_GearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting GearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
            parent: "GearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5243,
            )

            return self._parent._cast(
                _5243.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
        ) -> "GearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "GearSetCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5173.GearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearSetModalAnalysisAtASpeed]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5173.GearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearSetModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundModalAnalysisAtASpeed._Cast_GearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_GearSetCompoundModalAnalysisAtASpeed(self)

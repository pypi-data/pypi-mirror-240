"""SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4984,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4953,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysisAtAStiffness")


class SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(
    _4984.AbstractAssemblyCompoundModalAnalysisAtAStiffness
):
    """SpecialisedAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
            parent: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4984.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(_4994.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(
                _5004.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(_5005.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
        ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4953.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

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
    ) -> "List[_4953.SpecialisedAssemblyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.SpecialisedAssemblyModalAnalysisAtAStiffness]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysisAtAStiffness(self)

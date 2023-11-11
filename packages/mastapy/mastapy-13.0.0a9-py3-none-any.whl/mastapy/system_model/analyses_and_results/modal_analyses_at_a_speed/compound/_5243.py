"""AbstractAssemblyCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5322,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5113,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysisAtASpeed")


class AbstractAssemblyCompoundModalAnalysisAtASpeed(
    _5322.PartCompoundModalAnalysisAtASpeed
):
    """AbstractAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
            parent: "AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(_5250.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(_5253.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(
                _5286.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(
                _5300.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(_5337.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(_5345.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5113.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5113.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed(self)

"""SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6135,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6104,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"
)


class SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6135.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6135.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6156,
            )

            return self._parent._cast(
                _6156.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )

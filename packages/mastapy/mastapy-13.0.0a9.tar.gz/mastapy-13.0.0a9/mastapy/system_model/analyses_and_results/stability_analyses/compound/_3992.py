"""SpecialisedAssemblyCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3860


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundStabilityAnalysis")


class SpecialisedAssemblyCompoundStabilityAnalysis(
    _3894.AbstractAssemblyCompoundStabilityAnalysis
):
    """SpecialisedAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
            parent: "SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def belt_drive_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3904,
            )

            return self._parent._cast(_3904.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.CouplingCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CVTCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.FaceGearSetCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(
                _3951.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(
                _3974.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpringDamperCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.SynchroniserCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.TorqueConverterCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
        ) -> "SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3860.SpecialisedAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpecialisedAssemblyStabilityAnalysis]

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
    ) -> "List[_3860.SpecialisedAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpecialisedAssemblyStabilityAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundStabilityAnalysis._Cast_SpecialisedAssemblyCompoundStabilityAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundStabilityAnalysis(self)

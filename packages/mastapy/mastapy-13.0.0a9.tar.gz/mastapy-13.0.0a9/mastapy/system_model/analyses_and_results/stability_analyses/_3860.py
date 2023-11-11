"""SpecialisedAssemblyStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpecialisedAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyStabilityAnalysis")


class SpecialisedAssemblyStabilityAnalysis(_3760.AbstractAssemblyStabilityAnalysis):
    """SpecialisedAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyStabilityAnalysis")

    class _Cast_SpecialisedAssemblyStabilityAnalysis:
        """Special nested class for casting SpecialisedAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
            parent: "SpecialisedAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearSetStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BoltedJointStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CycloidalAssemblyStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearSetStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearSetStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearSetStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryGearSetStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RollingRingAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearSetStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
        ) -> "SpecialisedAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2473.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyStabilityAnalysis._Cast_SpecialisedAssemblyStabilityAnalysis":
        return self._Cast_SpecialisedAssemblyStabilityAnalysis(self)

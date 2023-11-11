"""AbstractAssemblyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AbstractAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2682


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundSystemDeflection")


class AbstractAssemblyCompoundSystemDeflection(_2928.PartCompoundSystemDeflection):
    """AbstractAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundSystemDeflection"
    )

    class _Cast_AbstractAssemblyCompoundSystemDeflection:
        """Special nested class for casting AbstractAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
            parent: "AbstractAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(_2855.AssemblyCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(_2868.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RootAssemblyCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
        ) -> "AbstractAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2682.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

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
    ) -> "List[_2682.AbstractAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection]

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
    ) -> "AbstractAssemblyCompoundSystemDeflection._Cast_AbstractAssemblyCompoundSystemDeflection":
        return self._Cast_AbstractAssemblyCompoundSystemDeflection(self)

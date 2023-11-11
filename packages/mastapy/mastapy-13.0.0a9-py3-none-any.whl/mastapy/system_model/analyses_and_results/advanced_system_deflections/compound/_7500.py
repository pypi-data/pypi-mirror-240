"""SpecialisedAssemblyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7402,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7370,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundAdvancedSystemDeflection")


class SpecialisedAssemblyCompoundAdvancedSystemDeflection(
    _7402.AbstractAssemblyCompoundAdvancedSystemDeflection
):
    """SpecialisedAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7402.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(_7412.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(_7423.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.CouplingCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.CVTCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(
                _7459.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.GearSetCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(_7527.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7370.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "List[_7370.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection(self)

"""SpecialisedAssemblyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7266
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SpecialisedAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyAdvancedSystemDeflection")


class SpecialisedAssemblyAdvancedSystemDeflection(
    _7266.AbstractAssemblyAdvancedSystemDeflection
):
    """SpecialisedAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def belt_drive_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(_7287.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.ClutchAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearSetAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.CouplingAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.CVTAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.FaceGearSetAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpringDamperAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SynchroniserAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.TorqueConverterAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyAdvancedSystemDeflection.TYPE"
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
    ) -> "SpecialisedAssemblyAdvancedSystemDeflection._Cast_SpecialisedAssemblyAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyAdvancedSystemDeflection(self)

"""SpecialisedAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpecialisedAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4131


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundPowerFlow")


class SpecialisedAssemblyCompoundPowerFlow(_4163.AbstractAssemblyCompoundPowerFlow):
    """SpecialisedAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundPowerFlow")

    class _Cast_SpecialisedAssemblyCompoundPowerFlow:
        """Special nested class for casting SpecialisedAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
            parent: "SpecialisedAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.RollingRingAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "SpecialisedAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4131.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

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
    ) -> "List[_4131.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

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
    ) -> "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow":
        return self._Cast_SpecialisedAssemblyCompoundPowerFlow(self)

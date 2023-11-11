"""GearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4261
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _360
    from mastapy.system_model.analyses_and_results.power_flows import _4091


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearSetCompoundPowerFlow")


class GearSetCompoundPowerFlow(_4261.SpecialisedAssemblyCompoundPowerFlow):
    """GearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundPowerFlow")

    class _Cast_GearSetCompoundPowerFlow:
        """Special nested class for casting GearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
            parent: "GearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearSetCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.FaceGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PlanetaryGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearSetCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "GearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_360.GearSetDutyCycleRating":
        """mastapy.gears.rating.GearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4091.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    def assembly_analysis_cases_ready(self: Self) -> "List[_4091.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    ) -> "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow":
        return self._Cast_GearSetCompoundPowerFlow(self)

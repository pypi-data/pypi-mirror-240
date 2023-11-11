"""ConicalGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _536
    from mastapy.system_model.analyses_and_results.power_flows import _4062


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearCompoundPowerFlow")


class ConicalGearCompoundPowerFlow(_4221.GearCompoundPowerFlow):
    """ConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundPowerFlow")

    class _Cast_ConicalGearCompoundPowerFlow:
        """Special nested class for casting ConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
            parent: "ConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4221.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(
                _4177.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.ZerolBevelGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
        ) -> "ConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_536.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_duty_cycle_rating(self: Self) -> "_536.ConicalGearDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4062.ConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4062.ConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearCompoundPowerFlow._Cast_ConicalGearCompoundPowerFlow":
        return self._Cast_ConicalGearCompoundPowerFlow(self)

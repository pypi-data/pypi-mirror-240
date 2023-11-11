"""KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4099


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow")


class KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow(
    _4197.ConicalGearSetCompoundPowerFlow
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow]

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
    ) -> "List[_4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearSetPowerFlow]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow(self)

"""AGMAGleasonConicalGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4035


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundPowerFlow")


class AGMAGleasonConicalGearSetCompoundPowerFlow(_4197.ConicalGearSetCompoundPowerFlow):
    """AGMAGleasonConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4035.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

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
    ) -> "List[_4035.AGMAGleasonConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow]

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
    ) -> "AGMAGleasonConicalGearSetCompoundPowerFlow._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearSetCompoundPowerFlow(self)

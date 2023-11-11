"""HypoidGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "HypoidGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.power_flows import _4095
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4225,
        _4226,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundPowerFlow")


class HypoidGearSetCompoundPowerFlow(_4169.AGMAGleasonConicalGearSetCompoundPowerFlow):
    """HypoidGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetCompoundPowerFlow")

    class _Cast_HypoidGearSetCompoundPowerFlow:
        """Special nested class for casting HypoidGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
            parent: "HypoidGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4169.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
        ) -> "HypoidGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2532.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4095.HypoidGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow]

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
    def hypoid_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4225.HypoidGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4226.HypoidGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4095.HypoidGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCompoundPowerFlow._Cast_HypoidGearSetCompoundPowerFlow":
        return self._Cast_HypoidGearSetCompoundPowerFlow(self)

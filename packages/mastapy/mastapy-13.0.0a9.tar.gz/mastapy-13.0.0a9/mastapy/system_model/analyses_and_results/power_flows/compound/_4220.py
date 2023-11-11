"""FlexiblePinAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4261
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "FlexiblePinAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.power_flows import _4088


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundPowerFlow")


class FlexiblePinAssemblyCompoundPowerFlow(_4261.SpecialisedAssemblyCompoundPowerFlow):
    """FlexiblePinAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundPowerFlow")

    class _Cast_FlexiblePinAssemblyCompoundPowerFlow:
        """Special nested class for casting FlexiblePinAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
            parent: "FlexiblePinAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
        ) -> "FlexiblePinAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2451.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_4088.FlexiblePinAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4088.FlexiblePinAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.FlexiblePinAssemblyPowerFlow]

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
    ) -> "FlexiblePinAssemblyCompoundPowerFlow._Cast_FlexiblePinAssemblyCompoundPowerFlow":
        return self._Cast_FlexiblePinAssemblyCompoundPowerFlow(self)

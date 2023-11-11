"""ClutchCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4200
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ClutchCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.power_flows import _4052


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundPowerFlow",)


Self = TypeVar("Self", bound="ClutchCompoundPowerFlow")


class ClutchCompoundPowerFlow(_4200.CouplingCompoundPowerFlow):
    """ClutchCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchCompoundPowerFlow")

    class _Cast_ClutchCompoundPowerFlow:
        """Special nested class for casting ClutchCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
            parent: "ClutchCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_compound_power_flow(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            return self._parent._cast(_4200.CouplingCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_compound_power_flow(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow",
        ) -> "ClutchCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4052.ClutchPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchPowerFlow]

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
    def assembly_analysis_cases(self: Self) -> "List[_4052.ClutchPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ClutchPowerFlow]

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
    def cast_to(self: Self) -> "ClutchCompoundPowerFlow._Cast_ClutchCompoundPowerFlow":
        return self._Cast_ClutchCompoundPowerFlow(self)

"""AbstractShaftCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4165
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AbstractShaftCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4031


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundPowerFlow",)


Self = TypeVar("Self", bound="AbstractShaftCompoundPowerFlow")


class AbstractShaftCompoundPowerFlow(_4165.AbstractShaftOrHousingCompoundPowerFlow):
    """AbstractShaftCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftCompoundPowerFlow")

    class _Cast_AbstractShaftCompoundPowerFlow:
        """Special nested class for casting AbstractShaftCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
            parent: "AbstractShaftCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            return self._parent._cast(_4165.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CycloidalDiscCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.ShaftCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
        ) -> "AbstractShaftCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4031.AbstractShaftPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftPowerFlow]

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
    ) -> "List[_4031.AbstractShaftPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftPowerFlow]

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
    ) -> "AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow":
        return self._Cast_AbstractShaftCompoundPowerFlow(self)

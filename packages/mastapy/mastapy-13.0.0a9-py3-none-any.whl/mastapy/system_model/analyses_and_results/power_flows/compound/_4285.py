"""VirtualComponentCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "VirtualComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4156


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="VirtualComponentCompoundPowerFlow")


class VirtualComponentCompoundPowerFlow(_4240.MountableComponentCompoundPowerFlow):
    """VirtualComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentCompoundPowerFlow")

    class _Cast_VirtualComponentCompoundPowerFlow:
        """Special nested class for casting VirtualComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
            parent: "VirtualComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            return self._parent._cast(_4240.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.MeasurementComponentCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.PowerLoadCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
        ) -> "VirtualComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4156.VirtualComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow]

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
    ) -> "List[_4156.VirtualComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow]

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
    ) -> "VirtualComponentCompoundPowerFlow._Cast_VirtualComponentCompoundPowerFlow":
        return self._Cast_VirtualComponentCompoundPowerFlow(self)

"""ClutchPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4068
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ClutchPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.static_loads import _6831
    from mastapy.system_model.analyses_and_results.power_flows import _4050


__docformat__ = "restructuredtext en"
__all__ = ("ClutchPowerFlow",)


Self = TypeVar("Self", bound="ClutchPowerFlow")


class ClutchPowerFlow(_4068.CouplingPowerFlow):
    """ClutchPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchPowerFlow")

    class _Cast_ClutchPowerFlow:
        """Special nested class for casting ClutchPowerFlow to subclasses."""

        def __init__(
            self: "ClutchPowerFlow._Cast_ClutchPowerFlow", parent: "ClutchPowerFlow"
        ):
            self._parent = parent

        @property
        def coupling_power_flow(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            return self._parent._cast(_4068.CouplingPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ClutchPowerFlow._Cast_ClutchPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4029

            return self._parent._cast(_4029.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ClutchPowerFlow._Cast_ClutchPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchPowerFlow._Cast_ClutchPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ClutchPowerFlow._Cast_ClutchPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_power_flow(
            self: "ClutchPowerFlow._Cast_ClutchPowerFlow",
        ) -> "ClutchPowerFlow":
            return self._parent

        def __getattr__(self: "ClutchPowerFlow._Cast_ClutchPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6831.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def clutch_connection(self: Self) -> "_4050.ClutchConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ClutchConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchPowerFlow._Cast_ClutchPowerFlow":
        return self._Cast_ClutchPowerFlow(self)

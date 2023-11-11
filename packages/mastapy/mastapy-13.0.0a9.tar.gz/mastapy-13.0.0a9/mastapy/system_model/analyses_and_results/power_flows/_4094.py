"""HypoidGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.gears.rating.hypoid import _437
    from mastapy.system_model.analyses_and_results.static_loads import _6902


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearPowerFlow")


class HypoidGearPowerFlow(_4034.AGMAGleasonConicalGearPowerFlow):
    """HypoidGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearPowerFlow")

    class _Cast_HypoidGearPowerFlow:
        """Special nested class for casting HypoidGearPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
            parent: "HypoidGearPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            return self._parent._cast(_4034.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def gear_power_flow(self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ComponentPowerFlow)

        @property
        def part_power_flow(self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_power_flow(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow",
        ) -> "HypoidGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_437.HypoidGearRating":
        """mastapy.gears.rating.hypoid.HypoidGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6902.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearPowerFlow._Cast_HypoidGearPowerFlow":
        return self._Cast_HypoidGearPowerFlow(self)

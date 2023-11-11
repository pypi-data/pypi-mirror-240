"""KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4098
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _404
    from mastapy.system_model.analyses_and_results.static_loads import _6915


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearPowerFlow")


class KlingelnbergCycloPalloidSpiralBevelGearPowerFlow(
    _4098.KlingelnbergCycloPalloidConicalGearPowerFlow
):
    """KlingelnbergCycloPalloidSpiralBevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_404.KlingelnbergCycloPalloidSpiralBevelGearRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6915.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearPowerFlow(self)

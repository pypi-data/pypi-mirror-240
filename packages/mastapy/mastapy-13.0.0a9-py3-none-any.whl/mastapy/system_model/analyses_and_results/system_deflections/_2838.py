"""ZerolBevelGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ZerolBevelGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.gears.rating.zerol_bevel import _368
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.power_flows import _4161


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearSystemDeflection")


class ZerolBevelGearSystemDeflection(_2705.BevelGearSystemDeflection):
    """ZerolBevelGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSystemDeflection")

    class _Cast_ZerolBevelGearSystemDeflection:
        """Special nested class for casting ZerolBevelGearSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
            parent: "ZerolBevelGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            return self._parent._cast(_2705.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
        ) -> "ZerolBevelGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_368.ZerolBevelGearRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6982.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4161.ZerolBevelGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ZerolBevelGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSystemDeflection._Cast_ZerolBevelGearSystemDeflection":
        return self._Cast_ZerolBevelGearSystemDeflection(self)

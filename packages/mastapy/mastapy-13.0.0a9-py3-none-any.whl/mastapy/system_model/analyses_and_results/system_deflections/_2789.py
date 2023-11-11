"""PowerLoadSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PowerLoadSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6936
    from mastapy.system_model.analyses_and_results.power_flows import _4120
    from mastapy.system_model.analyses_and_results.system_deflections import _2830


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadSystemDeflection")


class PowerLoadSystemDeflection(_2832.VirtualComponentSystemDeflection):
    """PowerLoadSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadSystemDeflection")

    class _Cast_PowerLoadSystemDeflection:
        """Special nested class for casting PowerLoadSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
            parent: "PowerLoadSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            return self._parent._cast(_2832.VirtualComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def power_load_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "PowerLoadSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2469.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6936.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4120.PowerLoadPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_error_to_other_power_loads(
        self: Self,
    ) -> "List[_2830.TransmissionErrorResult]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TransmissionErrorResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorToOtherPowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection":
        return self._Cast_PowerLoadSystemDeflection(self)

"""RollingRingAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "RollingRingAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.power_flows import _4124


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblySystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAssemblySystemDeflection")


class RollingRingAssemblySystemDeflection(_2803.SpecialisedAssemblySystemDeflection):
    """RollingRingAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblySystemDeflection")

    class _Cast_RollingRingAssemblySystemDeflection:
        """Special nested class for casting RollingRingAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
            parent: "RollingRingAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
        ) -> "RollingRingAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingAssemblySystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6942.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4124.RollingRingAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.RollingRingAssemblyPowerFlow

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
    ) -> (
        "RollingRingAssemblySystemDeflection._Cast_RollingRingAssemblySystemDeflection"
    ):
        return self._Cast_RollingRingAssemblySystemDeflection(self)

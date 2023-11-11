"""RollingRingAssemblyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "RollingRingAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.system_deflections import _2794


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAssemblyAdvancedSystemDeflection")


class RollingRingAssemblyAdvancedSystemDeflection(
    _7370.SpecialisedAssemblyAdvancedSystemDeflection
):
    """RollingRingAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyAdvancedSystemDeflection"
    )

    class _Cast_RollingRingAssemblyAdvancedSystemDeflection:
        """Special nested class for casting RollingRingAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
            parent: "RollingRingAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7370.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7266,
            )

            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ) -> "RollingRingAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyAdvancedSystemDeflection.TYPE"
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
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2794.RollingRingAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection":
        return self._Cast_RollingRingAssemblyAdvancedSystemDeflection(self)

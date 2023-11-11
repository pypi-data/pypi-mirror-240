"""UnbalancedMassAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7395
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "UnbalancedMassAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.system_deflections import _2831


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="UnbalancedMassAdvancedSystemDeflection")


class UnbalancedMassAdvancedSystemDeflection(
    _7395.VirtualComponentAdvancedSystemDeflection
):
    """UnbalancedMassAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassAdvancedSystemDeflection"
    )

    class _Cast_UnbalancedMassAdvancedSystemDeflection:
        """Special nested class for casting UnbalancedMassAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
            parent: "UnbalancedMassAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7395.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
        ) -> "UnbalancedMassAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "UnbalancedMassAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2474.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6977.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2831.UnbalancedMassSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassAdvancedSystemDeflection._Cast_UnbalancedMassAdvancedSystemDeflection":
        return self._Cast_UnbalancedMassAdvancedSystemDeflection(self)

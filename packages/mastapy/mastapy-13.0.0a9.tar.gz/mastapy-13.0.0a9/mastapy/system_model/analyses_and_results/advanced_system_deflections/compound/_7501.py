"""SpiralBevelGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7418,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7371,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundAdvancedSystemDeflection")


class SpiralBevelGearCompoundAdvancedSystemDeflection(
    _7418.BevelGearCompoundAdvancedSystemDeflection
):
    """SpiralBevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpiralBevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpiralBevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
            parent: "SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7418.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(_7434.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(_7460.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "SpiralBevelGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpiralBevelGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7371.SpiralBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpiralBevelGearAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7371.SpiralBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpiralBevelGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearCompoundAdvancedSystemDeflection._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection":
        return self._Cast_SpiralBevelGearCompoundAdvancedSystemDeflection(self)

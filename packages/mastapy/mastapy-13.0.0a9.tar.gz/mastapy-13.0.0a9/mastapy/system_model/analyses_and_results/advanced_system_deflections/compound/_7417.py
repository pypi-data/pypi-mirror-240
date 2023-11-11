"""BevelDifferentialSunGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7413,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7284,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundAdvancedSystemDeflection")


class BevelDifferentialSunGearCompoundAdvancedSystemDeflection(
    _7413.BevelDifferentialGearCompoundAdvancedSystemDeflection
):
    """BevelDifferentialSunGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialSunGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
            parent: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7413.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(_7418.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(_7434.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(_7460.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
        ) -> "BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7284.BevelDifferentialSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialSunGearAdvancedSystemDeflection]

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
    ) -> "List[_7284.BevelDifferentialSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialSunGearAdvancedSystemDeflection]

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
    ) -> "BevelDifferentialSunGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialSunGearCompoundAdvancedSystemDeflection(self)

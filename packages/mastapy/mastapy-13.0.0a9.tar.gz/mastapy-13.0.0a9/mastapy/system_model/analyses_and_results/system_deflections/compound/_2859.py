"""BevelDifferentialGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelDifferentialGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512
    from mastapy.system_model.analyses_and_results.system_deflections import _2700


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundSystemDeflection")


class BevelDifferentialGearCompoundSystemDeflection(
    _2864.BevelGearCompoundSystemDeflection
):
    """BevelDifferentialGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundSystemDeflection"
    )

    class _Cast_BevelDifferentialGearCompoundSystemDeflection:
        """Special nested class for casting BevelDifferentialGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
            parent: "BevelDifferentialGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
        ) -> "BevelDifferentialGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2512.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

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
    ) -> "List[_2700.BevelDifferentialGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection]

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
    ) -> "List[_2700.BevelDifferentialGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection]

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
    ) -> "BevelDifferentialGearCompoundSystemDeflection._Cast_BevelDifferentialGearCompoundSystemDeflection":
        return self._Cast_BevelDifferentialGearCompoundSystemDeflection(self)

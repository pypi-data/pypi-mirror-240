"""StraightBevelPlanetGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "StraightBevelPlanetGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2816


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundSystemDeflection")


class StraightBevelPlanetGearCompoundSystemDeflection(
    _2955.StraightBevelDiffGearCompoundSystemDeflection
):
    """StraightBevelPlanetGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundSystemDeflection"
    )

    class _Cast_StraightBevelPlanetGearCompoundSystemDeflection:
        """Special nested class for casting StraightBevelPlanetGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
            parent: "StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2955.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
        ) -> "StraightBevelPlanetGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2816.StraightBevelPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection]

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
    ) -> "List[_2816.StraightBevelPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection]

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
    ) -> "StraightBevelPlanetGearCompoundSystemDeflection._Cast_StraightBevelPlanetGearCompoundSystemDeflection":
        return self._Cast_StraightBevelPlanetGearCompoundSystemDeflection(self)

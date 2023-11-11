"""StraightBevelGearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "StraightBevelGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.system_deflections import _2815


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundSystemDeflection")


class StraightBevelGearCompoundSystemDeflection(
    _2864.BevelGearCompoundSystemDeflection
):
    """StraightBevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearCompoundSystemDeflection"
    )

    class _Cast_StraightBevelGearCompoundSystemDeflection:
        """Special nested class for casting StraightBevelGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
            parent: "StraightBevelGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def conical_gear_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
        ) -> "StraightBevelGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_2815.StraightBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection]

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
    ) -> "List[_2815.StraightBevelGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection]

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
    ) -> "StraightBevelGearCompoundSystemDeflection._Cast_StraightBevelGearCompoundSystemDeflection":
        return self._Cast_StraightBevelGearCompoundSystemDeflection(self)

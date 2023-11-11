"""BevelGearSetCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2704


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSetCompoundSystemDeflection")


class BevelGearSetCompoundSystemDeflection(
    _2854.AGMAGleasonConicalGearSetCompoundSystemDeflection
):
    """BevelGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundSystemDeflection")

    class _Cast_BevelGearSetCompoundSystemDeflection:
        """Special nested class for casting BevelGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
            parent: "BevelGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2854.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def conical_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2848,
            )

            return self._parent._cast(_2848.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
        ) -> "BevelGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2704.BevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2704.BevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundSystemDeflection._Cast_BevelGearSetCompoundSystemDeflection":
        return self._Cast_BevelGearSetCompoundSystemDeflection(self)

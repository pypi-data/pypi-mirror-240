"""GearCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "GearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _356
    from mastapy.system_model.analyses_and_results.system_deflections import _2758


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="GearCompoundSystemDeflection")


class GearCompoundSystemDeflection(_2926.MountableComponentCompoundSystemDeflection):
    """GearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundSystemDeflection")

    class _Cast_GearCompoundSystemDeflection:
        """Special nested class for casting GearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
            parent: "GearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(
                _2859.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(
                _2898.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def face_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.FaceGearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(_2958.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(
                _2962.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def worm_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.ZerolBevelGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
        ) -> "GearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_rating(self: Self) -> "_356.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_2758.GearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2758.GearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "GearCompoundSystemDeflection._Cast_GearCompoundSystemDeflection":
        return self._Cast_GearCompoundSystemDeflection(self)

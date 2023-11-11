"""GearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3822


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearCompoundStabilityAnalysis")


class GearCompoundStabilityAnalysis(_3971.MountableComponentCompoundStabilityAnalysis):
    """GearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundStabilityAnalysis")

    class _Cast_GearCompoundStabilityAnalysis:
        """Special nested class for casting GearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
            parent: "GearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def concept_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(
                _3944.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def face_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.FaceGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def worm_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ) -> "GearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_3822.GearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearStabilityAnalysis]

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
    ) -> "List[_3822.GearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearStabilityAnalysis]

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
    ) -> "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis":
        return self._Cast_GearCompoundStabilityAnalysis(self)

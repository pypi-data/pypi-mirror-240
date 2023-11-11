"""BevelDifferentialPlanetGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3905
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3774


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundStabilityAnalysis")


class BevelDifferentialPlanetGearCompoundStabilityAnalysis(
    _3905.BevelDifferentialGearCompoundStabilityAnalysis
):
    """BevelDifferentialPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3774.BevelDifferentialPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialPlanetGearStabilityAnalysis]

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
    ) -> "List[_3774.BevelDifferentialPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialPlanetGearStabilityAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis(self)

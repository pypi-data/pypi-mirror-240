"""ConicalGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3793


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundStabilityAnalysis")


class ConicalGearSetCompoundStabilityAnalysis(_3954.GearSetCompoundStabilityAnalysis):
    """ConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_ConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting ConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
            parent: "ConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "ConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3793.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3793.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    ) -> "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_ConicalGearSetCompoundStabilityAnalysis(self)

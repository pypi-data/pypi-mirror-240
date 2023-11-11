"""KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3829


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis(
    _3928.ConicalGearSetCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis(
                self
            )
        )

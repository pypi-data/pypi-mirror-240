"""BevelDifferentialSunGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6415
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelDifferentialSunGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundDynamicAnalysis")


class BevelDifferentialSunGearCompoundDynamicAnalysis(
    _6415.BevelDifferentialGearCompoundDynamicAnalysis
):
    """BevelDifferentialSunGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundDynamicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundDynamicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
            parent: "BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(
                _6415.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(
                _6408.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
        ) -> "BevelDifferentialSunGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6288.BevelDifferentialSunGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis]

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
    ) -> "List[_6288.BevelDifferentialSunGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundDynamicAnalysis._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundDynamicAnalysis(self)

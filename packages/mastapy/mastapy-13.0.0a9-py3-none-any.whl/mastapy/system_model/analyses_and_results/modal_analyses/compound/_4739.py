"""BevelDifferentialSunGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4735
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelDifferentialSunGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4583


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundModalAnalysis")


class BevelDifferentialSunGearCompoundModalAnalysis(
    _4735.BevelDifferentialGearCompoundModalAnalysis
):
    """BevelDifferentialSunGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundModalAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundModalAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
            parent: "BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            return self._parent._cast(_4735.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(_4801.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
        ) -> "BevelDifferentialSunGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4583.BevelDifferentialSunGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis]

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
    ) -> "List[_4583.BevelDifferentialSunGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundModalAnalysis._Cast_BevelDifferentialSunGearCompoundModalAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundModalAnalysis(self)

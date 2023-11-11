"""CouplingHalfCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3971
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CouplingHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3798


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundStabilityAnalysis")


class CouplingHalfCompoundStabilityAnalysis(
    _3971.MountableComponentCompoundStabilityAnalysis
):
    """CouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundStabilityAnalysis"
    )

    class _Cast_CouplingHalfCompoundStabilityAnalysis:
        """Special nested class for casting CouplingHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
            parent: "CouplingHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CVTPulleyCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def pulley_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PulleyCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.RollingRingCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(
                _4014.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def coupling_half_compound_stability_analysis(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
        ) -> "CouplingHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3798.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    ) -> "List[_3798.CouplingHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingHalfStabilityAnalysis]

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
    ) -> "CouplingHalfCompoundStabilityAnalysis._Cast_CouplingHalfCompoundStabilityAnalysis":
        return self._Cast_CouplingHalfCompoundStabilityAnalysis(self)

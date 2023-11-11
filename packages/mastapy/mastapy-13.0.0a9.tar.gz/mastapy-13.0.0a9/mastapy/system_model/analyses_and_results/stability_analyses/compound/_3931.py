"""CouplingCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3992
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CouplingCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3799


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundStabilityAnalysis")


class CouplingCompoundStabilityAnalysis(
    _3992.SpecialisedAssemblyCompoundStabilityAnalysis
):
    """CouplingCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundStabilityAnalysis")

    class _Cast_CouplingCompoundStabilityAnalysis:
        """Special nested class for casting CouplingCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
            parent: "CouplingCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(
                _3974.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def spring_damper_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpringDamperCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.TorqueConverterCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
        ) -> "CouplingCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_3799.CouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingStabilityAnalysis]

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
    ) -> "List[_3799.CouplingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CouplingStabilityAnalysis]

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
    ) -> "CouplingCompoundStabilityAnalysis._Cast_CouplingCompoundStabilityAnalysis":
        return self._Cast_CouplingCompoundStabilityAnalysis(self)

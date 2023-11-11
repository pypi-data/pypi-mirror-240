"""CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7235,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7044,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class CouplingCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7235.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7235.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7137,
            )

            return self._parent._cast(
                _7137.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7044.CouplingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7044.CouplingAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )

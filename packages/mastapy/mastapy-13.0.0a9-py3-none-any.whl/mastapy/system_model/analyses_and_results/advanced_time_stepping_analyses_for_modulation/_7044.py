"""CouplingAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7106,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.system_deflections import _2728


__docformat__ = "restructuredtext en"
__all__ = ("CouplingAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CouplingAdvancedTimeSteppingAnalysisForModulation")


class CouplingAdvancedTimeSteppingAnalysisForModulation(
    _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_CouplingAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2728.CouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingAdvancedTimeSteppingAnalysisForModulation(self)

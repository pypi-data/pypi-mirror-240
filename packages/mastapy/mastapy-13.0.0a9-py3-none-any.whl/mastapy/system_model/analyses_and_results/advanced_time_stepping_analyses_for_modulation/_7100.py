"""RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7106,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.system_deflections import _2794


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"
)


class RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6942.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2794.RollingRingAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection

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
    ) -> "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation(
            self
        )

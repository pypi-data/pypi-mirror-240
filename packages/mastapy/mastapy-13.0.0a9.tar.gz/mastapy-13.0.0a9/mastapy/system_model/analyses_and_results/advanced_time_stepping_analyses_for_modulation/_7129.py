"""UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7130,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.system_deflections import _2831


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="UnbalancedMassAdvancedTimeSteppingAnalysisForModulation")


class UnbalancedMassAdvancedTimeSteppingAnalysisForModulation(
    _7130.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
):
    """UnbalancedMassAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting UnbalancedMassAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
            parent: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7130.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
        ) -> "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2474.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6977.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2831.UnbalancedMassSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection

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
    ) -> "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_UnbalancedMassAdvancedTimeSteppingAnalysisForModulation(self)

"""CVTAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.system_deflections import _2731


__docformat__ = "restructuredtext en"
__all__ = ("CVTAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="CVTAdvancedTimeSteppingAnalysisForModulation")


class CVTAdvancedTimeSteppingAnalysisForModulation(
    _7017.BeltDriveAdvancedTimeSteppingAnalysisForModulation
):
    """CVTAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CVT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_CVTAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CVTAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
            parent: "CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7017.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CVTAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CVTAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2731.CVTSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection

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
    ) -> "CVTAdvancedTimeSteppingAnalysisForModulation._Cast_CVTAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CVTAdvancedTimeSteppingAnalysisForModulation(self)

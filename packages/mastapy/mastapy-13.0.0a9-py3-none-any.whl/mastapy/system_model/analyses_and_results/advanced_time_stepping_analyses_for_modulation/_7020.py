"""BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.system_model.analyses_and_results.system_deflections import _2699
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7018,
        _7019,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7025.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7025.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2513.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6821.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

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
    ) -> "_2699.BevelDifferentialGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7018.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.BevelDifferentialGearsAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> (
        "List[_7019.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]"
    ):
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.BevelDifferentialMeshesAdvancedTimeSteppingAnalysisForModulation
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )

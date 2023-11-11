"""AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7039,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510
    from mastapy.system_model.analyses_and_results.system_deflections import _2688


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"
)


class AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation(
    _7039.ConicalGearAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7039.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(
                _7018.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2510.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2688.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

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
    ) -> "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )

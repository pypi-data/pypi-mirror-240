"""StraightBevelSunGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6647
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "StraightBevelSunGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCriticalSpeedAnalysis")


class StraightBevelSunGearCriticalSpeedAnalysis(
    _6647.StraightBevelDiffGearCriticalSpeedAnalysis
):
    """StraightBevelSunGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelSunGearCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelSunGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
            parent: "StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6647.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
        ) -> "StraightBevelSunGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCriticalSpeedAnalysis._Cast_StraightBevelSunGearCriticalSpeedAnalysis":
        return self._Cast_StraightBevelSunGearCriticalSpeedAnalysis(self)

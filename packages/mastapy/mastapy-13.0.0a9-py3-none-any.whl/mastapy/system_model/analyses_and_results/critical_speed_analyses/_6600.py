"""GearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("GearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearCriticalSpeedAnalysis")


class GearCriticalSpeedAnalysis(_6619.MountableComponentCriticalSpeedAnalysis):
    """GearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCriticalSpeedAnalysis")

    class _Cast_GearCriticalSpeedAnalysis:
        """Special nested class for casting GearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
            parent: "GearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(
                _6553.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.BevelGearCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConicalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.FaceGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "GearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.Gear":
        """mastapy.system_model.part_model.gears.Gear

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
    ) -> "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis":
        return self._Cast_GearCriticalSpeedAnalysis(self)

"""KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6571
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis")


class KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis(
    _6571.ConicalGearCriticalSpeedAnalysis
):
    """KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6571.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis(self)

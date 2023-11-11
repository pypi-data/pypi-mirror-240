"""KlingelnbergCycloPalloidConicalGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearStabilityAnalysis(
    _3794.ConicalGearStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearStabilityAnalysis.TYPE",
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
    ) -> "KlingelnbergCycloPalloidConicalGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearStabilityAnalysis(self)

"""KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6912


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearStabilityAnalysis")


class KlingelnbergCycloPalloidHypoidGearStabilityAnalysis(
    _3830.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6912.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearStabilityAnalysis(self)

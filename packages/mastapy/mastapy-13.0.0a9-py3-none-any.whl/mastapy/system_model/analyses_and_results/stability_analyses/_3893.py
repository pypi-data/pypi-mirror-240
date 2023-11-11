"""ZerolBevelGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ZerolBevelGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.static_loads import _6982


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearStabilityAnalysis")


class ZerolBevelGearStabilityAnalysis(_3778.BevelGearStabilityAnalysis):
    """ZerolBevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearStabilityAnalysis")

    class _Cast_ZerolBevelGearStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
            parent: "ZerolBevelGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
        ) -> "ZerolBevelGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6982.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "ZerolBevelGearStabilityAnalysis._Cast_ZerolBevelGearStabilityAnalysis":
        return self._Cast_ZerolBevelGearStabilityAnalysis(self)

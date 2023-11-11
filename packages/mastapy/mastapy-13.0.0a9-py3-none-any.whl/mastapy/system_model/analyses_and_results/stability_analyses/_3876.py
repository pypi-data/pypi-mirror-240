"""StraightBevelPlanetGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3872
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearStabilityAnalysis")


class StraightBevelPlanetGearStabilityAnalysis(
    _3872.StraightBevelDiffGearStabilityAnalysis
):
    """StraightBevelPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearStabilityAnalysis"
    )

    class _Cast_StraightBevelPlanetGearStabilityAnalysis:
        """Special nested class for casting StraightBevelPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
            parent: "StraightBevelPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            return self._parent._cast(_3872.StraightBevelDiffGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "StraightBevelPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis":
        return self._Cast_StraightBevelPlanetGearStabilityAnalysis(self)

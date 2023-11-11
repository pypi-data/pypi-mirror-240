"""AGMAGleasonConicalGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearStabilityAnalysis")


class AGMAGleasonConicalGearStabilityAnalysis(_3794.ConicalGearStabilityAnalysis):
    """AGMAGleasonConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
            parent: "AGMAGleasonConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(
                _3774.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearStabilityAnalysis.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearStabilityAnalysis(self)

"""BevelDifferentialSunGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialSunGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearStabilityAnalysis")


class BevelDifferentialSunGearStabilityAnalysis(
    _3773.BevelDifferentialGearStabilityAnalysis
):
    """BevelDifferentialSunGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearStabilityAnalysis"
    )

    class _Cast_BevelDifferentialSunGearStabilityAnalysis:
        """Special nested class for casting BevelDifferentialSunGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
            parent: "BevelDifferentialSunGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            return self._parent._cast(_3773.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
        ) -> "BevelDifferentialSunGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearStabilityAnalysis._Cast_BevelDifferentialSunGearStabilityAnalysis":
        return self._Cast_BevelDifferentialSunGearStabilityAnalysis(self)

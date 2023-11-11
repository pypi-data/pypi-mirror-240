"""AGMAGleasonConicalGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2723
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510
    from mastapy.system_model.analyses_and_results.power_flows import _4034


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSystemDeflection")


class AGMAGleasonConicalGearSystemDeflection(_2723.ConicalGearSystemDeflection):
    """AGMAGleasonConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
            parent: "AGMAGleasonConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "AGMAGleasonConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4034.AGMAGleasonConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSystemDeflection(self)

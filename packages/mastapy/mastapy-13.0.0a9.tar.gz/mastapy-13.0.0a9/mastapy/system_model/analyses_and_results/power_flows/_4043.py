"""BevelDifferentialPlanetGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "BevelDifferentialPlanetGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearPowerFlow")


class BevelDifferentialPlanetGearPowerFlow(_4041.BevelDifferentialGearPowerFlow):
    """BevelDifferentialPlanetGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialPlanetGearPowerFlow")

    class _Cast_BevelDifferentialPlanetGearPowerFlow:
        """Special nested class for casting BevelDifferentialPlanetGearPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
            parent: "BevelDifferentialPlanetGearPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            return self._parent._cast(_4041.BevelDifferentialGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
        ) -> "BevelDifferentialPlanetGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow",
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
        self: Self, instance_to_wrap: "BevelDifferentialPlanetGearPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2514.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow":
        return self._Cast_BevelDifferentialPlanetGearPowerFlow(self)

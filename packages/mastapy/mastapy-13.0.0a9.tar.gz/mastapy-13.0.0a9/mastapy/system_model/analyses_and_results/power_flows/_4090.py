"""GearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4108
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("GearPowerFlow",)


Self = TypeVar("Self", bound="GearPowerFlow")


class GearPowerFlow(_4108.MountableComponentPowerFlow):
    """GearPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearPowerFlow")

    class _Cast_GearPowerFlow:
        """Special nested class for casting GearPowerFlow to subclasses."""

        def __init__(
            self: "GearPowerFlow._Cast_GearPowerFlow", parent: "GearPowerFlow"
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ComponentPowerFlow)

        @property
        def part_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearPowerFlow)

        @property
        def concept_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def cylindrical_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalPlanetGearPowerFlow)

        @property
        def face_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearPowerFlow)

        @property
        def hypoid_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelSunGearPowerFlow)

        @property
        def worm_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(self: "GearPowerFlow._Cast_GearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearPowerFlow)

        @property
        def gear_power_flow(
            self: "GearPowerFlow._Cast_GearPowerFlow",
        ) -> "GearPowerFlow":
            return self._parent

        def __getattr__(self: "GearPowerFlow._Cast_GearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

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
    def cast_to(self: Self) -> "GearPowerFlow._Cast_GearPowerFlow":
        return self._Cast_GearPowerFlow(self)

"""ComponentPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ComponentPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441


__docformat__ = "restructuredtext en"
__all__ = ("ComponentPowerFlow",)


Self = TypeVar("Self", bound="ComponentPowerFlow")


class ComponentPowerFlow(_4110.PartPowerFlow):
    """ComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentPowerFlow")

    class _Cast_ComponentPowerFlow:
        """Special nested class for casting ComponentPowerFlow to subclasses."""

        def __init__(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
            parent: "ComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4031

            return self._parent._cast(_4031.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearPowerFlow)

        @property
        def bearing_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.BearingPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearPowerFlow)

        @property
        def bolt_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.ConceptCouplingHalfPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def connector_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.CouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CVTPulleyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearPowerFlow)

        @property
        def fe_part_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.FEPartPowerFlow)

        @property
        def gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def mass_disc_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.OilSealPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.PartToPartShearCouplingHalfPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.RingPinsPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RollingRingPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.ShaftPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpringDamperHalfPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self: "ComponentPowerFlow._Cast_ComponentPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearPowerFlow)

        @property
        def component_power_flow(
            self: "ComponentPowerFlow._Cast_ComponentPowerFlow",
        ) -> "ComponentPowerFlow":
            return self._parent

        def __getattr__(self: "ComponentPowerFlow._Cast_ComponentPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2441.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentPowerFlow._Cast_ComponentPowerFlow":
        return self._Cast_ComponentPowerFlow(self)

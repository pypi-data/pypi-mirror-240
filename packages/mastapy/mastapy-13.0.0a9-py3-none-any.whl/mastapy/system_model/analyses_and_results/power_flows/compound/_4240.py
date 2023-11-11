"""MountableComponentCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4188
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MountableComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4108


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentCompoundPowerFlow")


class MountableComponentCompoundPowerFlow(_4188.ComponentCompoundPowerFlow):
    """MountableComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentCompoundPowerFlow")

    class _Cast_MountableComponentCompoundPowerFlow:
        """Special nested class for casting MountableComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
            parent: "MountableComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            return self._parent._cast(_4188.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(
                _4177.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelGearCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.CVTPulleyCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.FaceGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.GearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.MeasurementComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(
                _4245.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.RollingRingCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.ZerolBevelGearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "MountableComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4108.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4108.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow"
    ):
        return self._Cast_MountableComponentCompoundPowerFlow(self)

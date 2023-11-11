"""MountableComponentSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "MountableComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.fe import _2382
    from mastapy.system_model.analyses_and_results.power_flows import _4108


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentSystemDeflection")


class MountableComponentSystemDeflection(_2712.ComponentSystemDeflection):
    """MountableComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentSystemDeflection")

    class _Cast_MountableComponentSystemDeflection:
        """Special nested class for casting MountableComponentSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
            parent: "MountableComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2695,
            )

            return self._parent._cast(_2695.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTPulleySystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(_2776.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MeasurementComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.ShaftHubConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
        ) -> "MountableComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2461.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_part(self: Self) -> "_2754.FEPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFEPart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_fe_substructure_nodes(self: Self) -> "List[_2382.FESubstructureNode]":
        """List[mastapy.system_model.fe.FESubstructureNode]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerFESubstructureNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4108.MountableComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow

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
    ) -> "MountableComponentSystemDeflection._Cast_MountableComponentSystemDeflection":
        return self._Cast_MountableComponentSystemDeflection(self)

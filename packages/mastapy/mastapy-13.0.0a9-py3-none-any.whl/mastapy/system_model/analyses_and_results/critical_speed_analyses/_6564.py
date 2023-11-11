"""ComponentCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6621
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCriticalSpeedAnalysis")


class ComponentCriticalSpeedAnalysis(_6621.PartCriticalSpeedAnalysis):
    """ComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCriticalSpeedAnalysis")

    class _Cast_ComponentCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            parent: "ComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6541,
            )

            return self._parent._cast(_6541.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6547,
            )

            return self._parent._cast(_6547.BearingCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(
                _6553.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.BevelGearCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(_6558.BoltCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConicalGearCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.FaceGearCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.FEPartCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.GearCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.OilSealCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RollingRingCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
        ) -> "ComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis":
        return self._Cast_ComponentCriticalSpeedAnalysis(self)

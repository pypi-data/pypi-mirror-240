"""ComponentHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.modal_analyses import _4593
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
        _5861,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2712


__docformat__ = "restructuredtext en"
__all__ = ("ComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="ComponentHarmonicAnalysis")


class ComponentHarmonicAnalysis(_5784.PartHarmonicAnalysis):
    """ComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentHarmonicAnalysis")

    class _Cast_ComponentHarmonicAnalysis:
        """Special nested class for casting ComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
            parent: "ComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5676,
            )

            return self._parent._cast(_5676.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5677,
            )

            return self._parent._cast(_5677.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelGearHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(_5742.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.FaceGearHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.FEPartHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.GearHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(_5780.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.ZerolBevelGearHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis",
        ) -> "ComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentHarmonicAnalysis.TYPE"):
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
    def coupled_modal_analysis(self: Self) -> "_4593.ComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(self: Self) -> "_5861.HarmonicAnalysisResultsPropertyAccessor":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results.HarmonicAnalysisResultsPropertyAccessor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2712.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentHarmonicAnalysis._Cast_ComponentHarmonicAnalysis":
        return self._Cast_ComponentHarmonicAnalysis(self)

"""ComponentCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ComponentCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundDynamicAnalysis")


class ComponentCompoundDynamicAnalysis(_6483.PartCompoundDynamicAnalysis):
    """ComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundDynamicAnalysis")

    class _Cast_ComponentCompoundDynamicAnalysis:
        """Special nested class for casting ComponentCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
            parent: "ComponentCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6405,
            )

            return self._parent._cast(_6405.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6406,
            )

            return self._parent._cast(
                _6406.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(
                _6408.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bearing_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(_6412.BearingCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6415,
            )

            return self._parent._cast(
                _6415.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BevelGearCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(_6423.BoltCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.ClutchHalfCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConicalGearCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(
                _6454.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.FaceGearCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.FEPartCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.GearCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(
                _6470.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(_6479.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.OilSealCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(
                _6486.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(_6490.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.RollingRingCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(
                _6509.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(_6519.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(
                _6524.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.WormGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
        ) -> "ComponentCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6298.ComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis]

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
    ) -> "List[_6298.ComponentDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis]

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
    ) -> "ComponentCompoundDynamicAnalysis._Cast_ComponentCompoundDynamicAnalysis":
        return self._Cast_ComponentCompoundDynamicAnalysis(self)

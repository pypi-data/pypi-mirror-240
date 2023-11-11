"""PartCompoundAnalysis"""
from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartCompoundAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAnalysis",)


Self = TypeVar("Self", bound="PartCompoundAnalysis")


class PartCompoundAnalysis(_7539.DesignEntityCompoundAnalysis):
    """PartCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundAnalysis")

    class _Cast_PartCompoundAnalysis:
        """Special nested class for casting PartCompoundAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
            parent: "PartCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2848,
            )

            return self._parent._cast(_2848.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2850,
            )

            return self._parent._cast(
                _2850.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(_2855.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2856,
            )

            return self._parent._cast(_2856.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(
                _2859.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(_2868.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(
                _2898.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.OilSealCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(_2958.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(
                _2962.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(_2964.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(_2966.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(
                _2970.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(_2971.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3113,
            )

            return self._parent._cast(
                _3113.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3114,
            )

            return self._parent._cast(
                _3114.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3115,
            )

            return self._parent._cast(
                _3115.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3119,
            )

            return self._parent._cast(
                _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3121,
            )

            return self._parent._cast(
                _3121.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3123,
            )

            return self._parent._cast(
                _3123.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3127,
            )

            return self._parent._cast(
                _3127.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3132,
            )

            return self._parent._cast(_3132.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3133,
            )

            return self._parent._cast(
                _3133.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(_3154.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(_3164.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(_3171.GearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(_3208.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(
                _3218.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3372,
            )

            return self._parent._cast(
                _3372.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3373,
            )

            return self._parent._cast(
                _3373.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3374,
            )

            return self._parent._cast(
                _3374.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3376,
            )

            return self._parent._cast(
                _3376.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3378,
            )

            return self._parent._cast(
                _3378.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3379,
            )

            return self._parent._cast(
                _3379.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3380,
            )

            return self._parent._cast(
                _3380.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3382,
            )

            return self._parent._cast(
                _3382.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3386,
            )

            return self._parent._cast(
                _3386.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3388,
            )

            return self._parent._cast(
                _3388.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3390,
            )

            return self._parent._cast(
                _3390.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3391,
            )

            return self._parent._cast(
                _3391.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3392,
            )

            return self._parent._cast(
                _3392.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3393,
            )

            return self._parent._cast(
                _3393.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3395,
            )

            return self._parent._cast(
                _3395.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3422,
            )

            return self._parent._cast(
                _3422.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3446,
            )

            return self._parent._cast(
                _3446.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3480,
            )

            return self._parent._cast(
                _3480.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3492,
            )

            return self._parent._cast(
                _3492.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3631,
            )

            return self._parent._cast(
                _3631.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3632,
            )

            return self._parent._cast(
                _3632.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3633,
            )

            return self._parent._cast(
                _3633.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3635,
            )

            return self._parent._cast(
                _3635.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3637,
            )

            return self._parent._cast(
                _3637.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3638,
            )

            return self._parent._cast(
                _3638.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3639,
            )

            return self._parent._cast(
                _3639.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3641,
            )

            return self._parent._cast(
                _3641.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3644,
            )

            return self._parent._cast(
                _3644.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3645,
            )

            return self._parent._cast(
                _3645.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3647,
            )

            return self._parent._cast(
                _3647.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3649,
            )

            return self._parent._cast(
                _3649.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3650,
            )

            return self._parent._cast(
                _3650.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3651,
            )

            return self._parent._cast(
                _3651.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3652,
            )

            return self._parent._cast(
                _3652.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3654,
            )

            return self._parent._cast(
                _3654.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3662,
            )

            return self._parent._cast(
                _3662.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3676,
            )

            return self._parent._cast(
                _3676.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3681,
            )

            return self._parent._cast(
                _3681.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3686,
            )

            return self._parent._cast(
                _3686.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3703,
            )

            return self._parent._cast(
                _3703.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3723,
            )

            return self._parent._cast(
                _3723.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3726,
            )

            return self._parent._cast(
                _3726.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3733,
            )

            return self._parent._cast(
                _3733.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3739,
            )

            return self._parent._cast(
                _3739.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3742,
            )

            return self._parent._cast(
                _3742.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3754,
            )

            return self._parent._cast(
                _3754.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3757,
            )

            return self._parent._cast(
                _3757.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3895,
            )

            return self._parent._cast(_3895.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3896,
            )

            return self._parent._cast(
                _3896.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(_3901.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(_3902.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3904,
            )

            return self._parent._cast(_3904.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(
                _3944.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(
                _3951.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.OilSealCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(
                _3974.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(_3988.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(_3990.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(
                _4014.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4163,
            )

            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4165,
            )

            return self._parent._cast(_4165.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.BearingCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(
                _4177.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.ClutchCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.ClutchHalfCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearSetCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.CouplingCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CycloidalDiscCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.FaceGearCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.GearCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(_4238.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.OilSealCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(
                _4245.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.RollingRingCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.ShaftHubConnectionCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.WormGearCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4439,
            )

            return self._parent._cast(_4439.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4440,
            )

            return self._parent._cast(_4440.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4441,
            )

            return self._parent._cast(
                _4441.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(
                _4443.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(_4446.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(_4447.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(_4449.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(
                _4450.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(
                _4452.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(_4457.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(_4460.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(
                _4482.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(
                _4489.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(
                _4496.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(
                _4507.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(_4514.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.OilSealCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(_4525.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(
                _4530.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(_4533.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(_4534.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(_4541.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(_4552.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(_4554.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(_4561.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(_4562.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4724,
            )

            return self._parent._cast(_4724.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4726,
            )

            return self._parent._cast(_4726.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(
                _4730.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(_4731.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(
                _4737.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(
                _4738.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(
                _4739.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(_4742.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(_4743.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(_4745.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(
                _4790.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(
                _4792.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(_4799.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(_4801.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.OilSealCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.PartCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(
                _4804.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(
                _4806.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(_4810.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(_4818.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(
                _4831.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4984,
            )

            return self._parent._cast(
                _4984.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4985,
            )

            return self._parent._cast(
                _4985.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4986,
            )

            return self._parent._cast(
                _4986.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(_4991.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(_4992.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(_4994.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4995,
            )

            return self._parent._cast(
                _4995.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(
                _4998.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4999,
            )

            return self._parent._cast(
                _4999.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(_5000.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(_5003.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(
                _5004.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(_5005.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(_5007.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(_5009.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(
                _5013.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(_5020.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(_5021.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(
                _5023.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(_5026.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(
                _5034.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(_5035.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(_5037.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(_5040.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(
                _5041.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(_5042.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(
                _5048.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(
                _5050.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(_5059.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(_5062.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(
                _5069.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(_5070.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(_5072.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(_5073.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(
                _5076.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(_5079.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(
                _5083.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(_5107.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5243,
            )

            return self._parent._cast(
                _5243.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5244,
            )

            return self._parent._cast(_5244.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5245,
            )

            return self._parent._cast(
                _5245.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(_5250.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(_5251.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(_5253.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5254,
            )

            return self._parent._cast(
                _5254.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(_5259.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(_5262.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(_5266.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(
                _5286.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(
                _5293.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(_5296.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(_5299.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(
                _5300.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(_5318.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(_5321.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(_5329.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(_5335.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(_5337.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(_5338.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(_5345.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(_5364.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(_5366.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(_5369.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5525,
            )

            return self._parent._cast(
                _5525.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5527,
            )

            return self._parent._cast(
                _5527.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(_5532.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(_5533.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(_5535.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5536,
            )

            return self._parent._cast(
                _5536.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(
                _5539.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(_5541.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(_5544.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(
                _5545.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(_5546.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(_5548.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(
                _5554.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(_5561.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(
                _5564.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(_5567.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(_5576.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(_5578.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(
                _5580.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(_5581.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(
                _5582.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(_5583.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(
                _5591.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(_5600.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(_5603.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(_5611.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(_5612.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(_5613.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(_5614.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(
                _5616.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(
                _5617.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(_5620.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(_5648.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5875,
            )

            return self._parent._cast(_5875.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5876,
            )

            return self._parent._cast(_5876.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5877,
            )

            return self._parent._cast(
                _5877.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(
                _5879.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(
                _5881.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(_5882.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(_5883.BearingCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5885,
            )

            return self._parent._cast(_5885.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5886,
            )

            return self._parent._cast(
                _5886.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(
                _5888.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(
                _5889.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(_5891.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(_5893.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(_5894.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5898,
            )

            return self._parent._cast(_5898.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(
                _5925.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.GearCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(
                _5943.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(_5950.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(
                _5951.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(_5952.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.OilSealCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.PartCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(
                _5957.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(_5959.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(_5961.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.RingPinsCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.RollingRingCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(_5969.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(_5971.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(_5973.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(
                _5980.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(
                _5987.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(_5988.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(_5990.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(_5991.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(_5994.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(
                _5995.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(_5996.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6135,
            )

            return self._parent._cast(
                _6135.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6136,
            )

            return self._parent._cast(
                _6136.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6137,
            )

            return self._parent._cast(
                _6137.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6142,
            )

            return self._parent._cast(
                _6142.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6143,
            )

            return self._parent._cast(
                _6143.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6146,
            )

            return self._parent._cast(
                _6146.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6150,
            )

            return self._parent._cast(
                _6150.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6156,
            )

            return self._parent._cast(
                _6156.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6187,
            )

            return self._parent._cast(
                _6187.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6210,
            )

            return self._parent._cast(
                _6210.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6211,
            )

            return self._parent._cast(
                _6211.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6221,
            )

            return self._parent._cast(
                _6221.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6230,
            )

            return self._parent._cast(
                _6230.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6247,
            )

            return self._parent._cast(
                _6247.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6250,
            )

            return self._parent._cast(
                _6250.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6256,
            )

            return self._parent._cast(
                _6256.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6404,
            )

            return self._parent._cast(_6404.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6405,
            )

            return self._parent._cast(_6405.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6406,
            )

            return self._parent._cast(
                _6406.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(
                _6408.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(
                _6410.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(_6411.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(_6412.BearingCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(_6414.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6415,
            )

            return self._parent._cast(
                _6415.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(
                _6417.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(_6420.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(_6422.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(_6423.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(_6425.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.ClutchHalfCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(
                _6454.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.GearCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(
                _6470.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(_6479.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(_6480.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.OilSealCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(
                _6486.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(_6490.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.RingPinsCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.RollingRingCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(_6498.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(
                _6509.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(_6519.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(
                _6524.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(_6526.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6671,
            )

            return self._parent._cast(
                _6671.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6672,
            )

            return self._parent._cast(_6672.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6673,
            )

            return self._parent._cast(
                _6673.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6677,
            )

            return self._parent._cast(
                _6677.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(_6678.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(_6679.BearingCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(_6681.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(
                _6682.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(
                _6684.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(_6687.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(_6689.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(_6690.BoltCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(_6692.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(_6703.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(_6705.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(_6707.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(_6708.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(
                _6714.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(
                _6720.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(
                _6721.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(_6724.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(_6727.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(
                _6728.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(_6729.GearCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(
                _6737.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(
                _6739.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(_6746.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(_6749.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(_6757.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(_6758.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(
                _6762.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(_6765.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(_6766.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(
                _6769.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(_6773.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(_6784.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6792,
            )

            return self._parent._cast(_6792.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(_6794.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(_6797.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7137,
            )

            return self._parent._cast(
                _7137.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7138,
            )

            return self._parent._cast(
                _7138.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7139,
            )

            return self._parent._cast(
                _7139.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7141,
            )

            return self._parent._cast(
                _7141.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7144,
            )

            return self._parent._cast(
                _7144.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7145,
            )

            return self._parent._cast(
                _7145.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7148,
            )

            return self._parent._cast(
                _7148.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7151,
            )

            return self._parent._cast(
                _7151.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7152,
            )

            return self._parent._cast(
                _7152.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7187,
            )

            return self._parent._cast(
                _7187.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7188,
            )

            return self._parent._cast(
                _7188.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7193,
            )

            return self._parent._cast(
                _7193.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7233,
            )

            return self._parent._cast(
                _7233.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7236,
            )

            return self._parent._cast(
                _7236.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7402,
            )

            return self._parent._cast(
                _7402.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7404,
            )

            return self._parent._cast(
                _7404.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(_7409.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(_7410.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(_7412.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7413,
            )

            return self._parent._cast(
                _7413.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(
                _7416.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7417,
            )

            return self._parent._cast(
                _7417.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(_7418.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(_7421.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(_7423.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(_7425.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(_7434.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(_7444.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(
                _7449.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(
                _7452.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(_7453.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(_7455.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(_7458.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(
                _7459.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(_7460.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(
                _7463.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(
                _7468.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(_7477.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(_7480.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.PartCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(
                _7487.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(_7488.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(_7489.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(_7491.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.RootAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(_7497.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(
                _7498.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(
                _7500.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(
                _7501.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(_7525.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(_7527.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_analysis(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis",
        ) -> "PartCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundAnalysis._Cast_PartCompoundAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PartCompoundAnalysis._Cast_PartCompoundAnalysis":
        return self._Cast_PartCompoundAnalysis(self)

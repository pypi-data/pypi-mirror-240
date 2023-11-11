"""PartCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PartCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PartCompoundSystemDeflection")


class PartCompoundSystemDeflection(_7542.PartCompoundAnalysis):
    """PartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundSystemDeflection")

    class _Cast_PartCompoundSystemDeflection:
        """Special nested class for casting PartCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
            parent: "PartCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2848,
            )

            return self._parent._cast(_2848.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2850,
            )

            return self._parent._cast(
                _2850.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(
                _2852.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(_2855.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2856,
            )

            return self._parent._cast(_2856.BearingCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(
                _2859.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(
                _2861.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(_2864.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(_2866.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(_2868.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.ClutchCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.ClutchHalfCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConicalGearSetCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.CouplingCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(
                _2898.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.GearCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(_2924.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(
                _2929.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(
                _2931.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.RollingRingCompoundSystemDeflection)

        @property
        def root_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(
                _2957.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(_2958.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(
                _2962.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(_2964.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(_2966.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(
                _2970.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(_2971.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(_2973.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
        ) -> "PartCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2782.PartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    ) -> "List[_2782.PartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection]

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
    ) -> "PartCompoundSystemDeflection._Cast_PartCompoundSystemDeflection":
        return self._Cast_PartCompoundSystemDeflection(self)

"""PartCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PartCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3841


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PartCompoundStabilityAnalysis")


class PartCompoundStabilityAnalysis(_7542.PartCompoundAnalysis):
    """PartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundStabilityAnalysis")

    class _Cast_PartCompoundStabilityAnalysis:
        """Special nested class for casting PartCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
            parent: "PartCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3894,
            )

            return self._parent._cast(_3894.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3895,
            )

            return self._parent._cast(_3895.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3896,
            )

            return self._parent._cast(
                _3896.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(_3901.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(_3902.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3904,
            )

            return self._parent._cast(_3904.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(
                _3944.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(
                _3951.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(
                _3974.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(_3988.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(_3990.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(
                _4014.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "PartCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_3841.PartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartStabilityAnalysis]

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
    ) -> "List[_3841.PartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartStabilityAnalysis]

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
    ) -> "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis":
        return self._Cast_PartCompoundStabilityAnalysis(self)

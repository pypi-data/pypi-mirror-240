"""PartStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.stability_analyses import _3867
    from mastapy.system_model.drawing import _2254


__docformat__ = "restructuredtext en"
__all__ = ("PartStabilityAnalysis",)


Self = TypeVar("Self", bound="PartStabilityAnalysis")


class PartStabilityAnalysis(_7544.PartStaticLoadAnalysisCase):
    """PartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartStabilityAnalysis")

    class _Cast_PartStabilityAnalysis:
        """Special nested class for casting PartStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
            parent: "PartStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3762,
            )

            return self._parent._cast(_3762.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(_3768.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(
                _3774.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis",
        ) -> "PartStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartStabilityAnalysis._Cast_PartStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis(self: Self) -> "_3867.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2254.StabilityAnalysisViewable":
        """mastapy.system_model.drawing.StabilityAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartStabilityAnalysis._Cast_PartStabilityAnalysis":
        return self._Cast_PartStabilityAnalysis(self)

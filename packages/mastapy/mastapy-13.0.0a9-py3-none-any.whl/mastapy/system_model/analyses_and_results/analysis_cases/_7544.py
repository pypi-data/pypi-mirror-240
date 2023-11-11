"""PartStaticLoadAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "PartStaticLoadAnalysisCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("PartStaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="PartStaticLoadAnalysisCase")


class PartStaticLoadAnalysisCase(_7541.PartAnalysisCase):
    """PartStaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _PART_STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartStaticLoadAnalysisCase")

    class _Cast_PartStaticLoadAnalysisCase:
        """Special nested class for casting PartStaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
            parent: "PartStaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2683,
            )

            return self._parent._cast(_2683.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2684,
            )

            return self._parent._cast(_2684.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2695,
            )

            return self._parent._cast(_2695.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(_2776.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(_2798.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2981,
            )

            return self._parent._cast(
                _2981.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2982,
            )

            return self._parent._cast(_2982.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(_2987.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2988,
            )

            return self._parent._cast(_2988.BearingSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(_2990.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(
                _2993.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(_2997.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(_3000.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(_3002.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(_3003.ClutchSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(
                _3008.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(_3011.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(_3018.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(_3019.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(_3021.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(
                _3023.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(_3026.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(
                _3029.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3030,
            )

            return self._parent._cast(
                _3030.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(_3035.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(_3036.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3037,
            )

            return self._parent._cast(_3037.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(
                _3038.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3049,
            )

            return self._parent._cast(
                _3049.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(_3056.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(_3059.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(_3066.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(_3069.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(_3074.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(_3075.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3076,
            )

            return self._parent._cast(
                _3076.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(_3077.ShaftSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(_3085.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(
                _3097.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(
                _3098.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(
                _3099.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(_3100.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3104,
            )

            return self._parent._cast(
                _3104.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(_3108.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(_3109.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3243,
            )

            return self._parent._cast(
                _3243.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3244,
            )

            return self._parent._cast(
                _3244.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3248,
            )

            return self._parent._cast(
                _3248.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3254,
            )

            return self._parent._cast(
                _3254.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3256,
            )

            return self._parent._cast(
                _3256.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(_3262.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3269,
            )

            return self._parent._cast(
                _3269.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(_3284.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3292,
            )

            return self._parent._cast(
                _3292.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(_3293.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3294,
            )

            return self._parent._cast(
                _3294.ExternalCADModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3297,
            )

            return self._parent._cast(
                _3297.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(_3302.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(
                _3303.GuideDxfModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(
                _3310.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(
                _3313.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3317,
            )

            return self._parent._cast(
                _3317.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(
                _3328.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3337,
            )

            return self._parent._cast(
                _3337.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(_3338.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3342,
            )

            return self._parent._cast(
                _3342.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3354,
            )

            return self._parent._cast(
                _3354.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3363,
            )

            return self._parent._cast(
                _3363.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3367,
            )

            return self._parent._cast(
                _3367.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3501,
            )

            return self._parent._cast(
                _3501.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3503,
            )

            return self._parent._cast(
                _3503.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3509,
            )

            return self._parent._cast(
                _3509.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(_3521.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(_3543.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(_3552.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(_3561.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(_3597.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3762,
            )

            return self._parent._cast(_3762.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(_3768.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(
                _3774.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4029

            return self._parent._cast(_4029.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4031

            return self._parent._cast(_4031.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AssemblyPowerFlow)

        @property
        def bearing_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.BearingPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BoltPowerFlow)

        @property
        def clutch_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchPowerFlow)

        @property
        def component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4056

            return self._parent._cast(_4056.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(_4101.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(
                _4102.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(_4106.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4107

            return self._parent._cast(_4107.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(_4108.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.OilSealPowerFlow)

        @property
        def part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(_4129.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4136

            return self._parent._cast(_4136.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4570

            return self._parent._cast(_4570.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(
                _4641.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(_4648.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.OilSealModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4675

            return self._parent._cast(_4675.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4853,
            )

            return self._parent._cast(_4853.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4854,
            )

            return self._parent._cast(_4854.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4855,
            )

            return self._parent._cast(
                _4855.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4860,
            )

            return self._parent._cast(_4860.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4861,
            )

            return self._parent._cast(_4861.BearingModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(_4863.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(
                _4866.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4867,
            )

            return self._parent._cast(
                _4867.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(_4870.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(_4871.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(_4872.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4873,
            )

            return self._parent._cast(_4873.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(_4876.ClutchModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(_4898.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(_4901.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4903,
            )

            return self._parent._cast(
                _4903.CylindricalPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def datum_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4904,
            )

            return self._parent._cast(_4904.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(
                _4911.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(
                _4921.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(
                _4928.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(_4929.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(
                _4930.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(
                _4937.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(_4939.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(_4941.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4942,
            )

            return self._parent._cast(_4942.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(_4948.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4949,
            )

            return self._parent._cast(_4949.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(_4950.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4951,
            )

            return self._parent._cast(_4951.ShaftModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(
                _4953.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(_4955.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(_4958.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(_4964.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(_4968.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(_4969.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(_4970.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(_4971.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(_4973.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(
                _4974.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(
                _4975.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4976,
            )

            return self._parent._cast(_4976.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(_4979.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5113,
            )

            return self._parent._cast(_5113.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5115,
            )

            return self._parent._cast(_5115.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(_5118.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(
                _5119.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(_5120.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5121,
            )

            return self._parent._cast(_5121.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(_5123.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5126,
            )

            return self._parent._cast(
                _5126.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5127,
            )

            return self._parent._cast(
                _5127.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5128,
            )

            return self._parent._cast(
                _5128.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(_5131.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(_5132.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5133,
            )

            return self._parent._cast(_5133.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5152,
            )

            return self._parent._cast(_5152.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5163,
            )

            return self._parent._cast(_5163.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5164,
            )

            return self._parent._cast(_5164.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5170,
            )

            return self._parent._cast(_5170.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(
                _5180.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(
                _5181.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(
                _5187.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5189,
            )

            return self._parent._cast(_5189.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(
                _5195.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(
                _5196.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(_5200.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5201,
            )

            return self._parent._cast(_5201.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5208,
            )

            return self._parent._cast(_5208.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(_5209.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5210,
            )

            return self._parent._cast(_5210.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5215,
            )

            return self._parent._cast(_5215.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(_5220.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(
                _5221.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(
                _5225.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(_5229.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(_5232.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5676,
            )

            return self._parent._cast(_5676.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5677,
            )

            return self._parent._cast(_5677.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5679,
            )

            return self._parent._cast(_5679.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(_5742.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(_5743.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(_5745.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5756,
            )

            return self._parent._cast(_5756.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(
                _5773.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(_5780.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(_5781.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(_5801.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6004,
            )

            return self._parent._cast(
                _6004.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6006,
            )

            return self._parent._cast(
                _6006.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(_6011.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(_6012.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(_6014.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(
                _6015.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6017,
            )

            return self._parent._cast(
                _6017.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(
                _6018.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(_6020.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(_6024.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(_6027.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(
                _6031.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(
                _6033.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(_6040.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(_6043.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(_6045.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(_6046.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(
                _6047.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6054,
            )

            return self._parent._cast(
                _6054.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(_6055.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(_6057.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(
                _6059.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(_6060.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(
                _6061.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(_6062.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(
                _6067.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6074,
            )

            return self._parent._cast(
                _6074.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(_6080.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(_6084.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(
                _6090.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(_6094.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(_6095.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(
                _6099.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(
                _6100.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(_6101.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6102,
            )

            return self._parent._cast(
                _6102.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(
                _6107.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(_6129.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273

            return self._parent._cast(_6273.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275

            return self._parent._cast(_6275.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6539,
            )

            return self._parent._cast(_6539.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6541,
            )

            return self._parent._cast(_6541.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6546,
            )

            return self._parent._cast(_6546.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6547,
            )

            return self._parent._cast(_6547.BearingCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(_6549.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6552,
            )

            return self._parent._cast(
                _6552.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(
                _6553.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(_6555.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(_6557.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(_6558.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(_6559.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.ClutchHalfCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(_6566.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6600,
            )

            return self._parent._cast(_6600.GearCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(
                _6610.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6611,
            )

            return self._parent._cast(
                _6611.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6616,
            )

            return self._parent._cast(
                _6616.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(_6617.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(_6618.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(
                _6623.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(_6626.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(_6628.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6629,
            )

            return self._parent._cast(_6629.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6638,
            )

            return self._parent._cast(_6638.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(
                _6649.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7004,
            )

            return self._parent._cast(
                _7004.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7010,
            )

            return self._parent._cast(
                _7010.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7013,
            )

            return self._parent._cast(
                _7013.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7015,
            )

            return self._parent._cast(
                _7015.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(
                _7018.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BoltAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.DatumAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7266,
            )

            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7268,
            )

            return self._parent._cast(
                _7268.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(
                _7273.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7276,
            )

            return self._parent._cast(_7276.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(_7277.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(_7279.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(
                _7280.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(
                _7283.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(_7285.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(_7287.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(_7288.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7290,
            )

            return self._parent._cast(_7290.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(_7310.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(
                _7321.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(
                _7339.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(
                _7342.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(_7366.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(_7367.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(
                _7377.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(
                _7392.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(_7394.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
        ) -> "PartStaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartStaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartStaticLoadAnalysisCase._Cast_PartStaticLoadAnalysisCase":
        return self._Cast_PartStaticLoadAnalysisCase(self)

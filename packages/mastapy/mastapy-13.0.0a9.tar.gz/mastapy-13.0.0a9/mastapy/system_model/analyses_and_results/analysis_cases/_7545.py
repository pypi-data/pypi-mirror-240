"""PartTimeSeriesLoadAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "PartTimeSeriesLoadAnalysisCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("PartTimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="PartTimeSeriesLoadAnalysisCase")


class PartTimeSeriesLoadAnalysisCase(_7541.PartAnalysisCase):
    """PartTimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _PART_TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartTimeSeriesLoadAnalysisCase")

    class _Cast_PartTimeSeriesLoadAnalysisCase:
        """Special nested class for casting PartTimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
            parent: "PartTimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372

            return self._parent._cast(_5372.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373

            return self._parent._cast(_5373.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5374

            return self._parent._cast(
                _5374.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(
                _5377.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(_5380.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(_5381.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(_5391.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(_5394.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(
                _5402.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(_5423.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(_5426.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(
                _5432.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(_5455.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(
                _5459.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462

            return self._parent._cast(_5462.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(_5470.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(_5471.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(_5477.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(_5481.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(_5487.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(_5490.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(
                _5507.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(
                _5509.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(_5510.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(_5511.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
        ) -> "PartTimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartTimeSeriesLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PartTimeSeriesLoadAnalysisCase._Cast_PartTimeSeriesLoadAnalysisCase":
        return self._Cast_PartTimeSeriesLoadAnalysisCase(self)

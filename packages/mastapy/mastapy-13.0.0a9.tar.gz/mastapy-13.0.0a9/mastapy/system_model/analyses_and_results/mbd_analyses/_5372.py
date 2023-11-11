"""AbstractAssemblyMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AbstractAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyMultibodyDynamicsAnalysis")


class AbstractAssemblyMultibodyDynamicsAnalysis(_5463.PartMultibodyDynamicsAnalysis):
    """AbstractAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
            parent: "AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(_5380.AssemblyMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(_5393.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.ClutchMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CVTMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(
                _5432.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(
                _5448.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(
                _5466.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(_5501.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
        ) -> "AbstractAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2431.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2431.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_AbstractAssemblyMultibodyDynamicsAnalysis(self)

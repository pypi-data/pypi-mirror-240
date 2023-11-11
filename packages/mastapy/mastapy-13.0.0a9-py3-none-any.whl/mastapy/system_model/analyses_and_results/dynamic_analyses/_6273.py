"""AbstractAssemblyDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractAssemblyDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyDynamicAnalysis")


class AbstractAssemblyDynamicAnalysis(_6354.PartDynamicAnalysis):
    """AbstractAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyDynamicAnalysis")

    class _Cast_AbstractAssemblyDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            parent: "AbstractAssemblyDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AssemblyDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearSetDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ConceptCouplingDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearSetDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.CouplingDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.CVTDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CycloidalAssemblyDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.FaceGearSetDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.PartToPartShearCouplingDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PlanetaryGearSetDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.RollingRingAssemblyDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.RootAssemblyDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpringDamperDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearSetDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.SynchroniserDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.TorqueConverterDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
        ) -> "AbstractAssemblyDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyDynamicAnalysis.TYPE"):
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
    ) -> "AbstractAssemblyDynamicAnalysis._Cast_AbstractAssemblyDynamicAnalysis":
        return self._Cast_AbstractAssemblyDynamicAnalysis(self)

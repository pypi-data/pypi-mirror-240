"""AbstractAssemblyModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4658
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431
    from mastapy.system_model.analyses_and_results.modal_analyses import _4631, _4593
    from mastapy.system_model.analyses_and_results.system_deflections import _2682


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyModalAnalysis")


class AbstractAssemblyModalAnalysis(_4658.PartModalAnalysis):
    """AbstractAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyModalAnalysis")

    class _Cast_AbstractAssemblyModalAnalysis:
        """Special nested class for casting AbstractAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            parent: "AbstractAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AssemblyModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BoltedJointModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CVTModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CycloidalAssemblyModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CylindricalGearSetModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.FaceGearSetModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629

            return self._parent._cast(_4629.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(
                _4641.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(_4663.PlanetaryGearSetModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.RollingRingAssemblyModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.RootAssemblyModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearSetModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.SynchroniserModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.TorqueConverterModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
        ) -> "AbstractAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyModalAnalysis.TYPE"):
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
    def gear_meshes(self: Self) -> "List[_4631.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(self: Self) -> "List[_4593.ComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2682.AbstractAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection

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
    ) -> "AbstractAssemblyModalAnalysis._Cast_AbstractAssemblyModalAnalysis":
        return self._Cast_AbstractAssemblyModalAnalysis(self)

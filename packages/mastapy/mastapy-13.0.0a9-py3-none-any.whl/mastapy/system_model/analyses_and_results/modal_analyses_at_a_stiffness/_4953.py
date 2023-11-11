"""SpecialisedAssemblyModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4853,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SpecialisedAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysisAtAStiffness")


class SpecialisedAssemblyModalAnalysisAtAStiffness(
    _4853.AbstractAssemblyModalAnalysisAtAStiffness
):
    """SpecialisedAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_SpecialisedAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting SpecialisedAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
            parent: "SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4853.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(_4863.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(
                _4866.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(_4871.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(_4872.BoltedJointModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(_4876.ClutchModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(_4884.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CVTModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4909,
            )

            return self._parent._cast(_4909.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(
                _4911.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(
                _4922.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(
                _4928.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(
                _4937.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4939,
            )

            return self._parent._cast(_4939.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(_4969.SynchroniserModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(_4973.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
        ) -> "SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "SpecialisedAssemblyModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2473.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

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
    ) -> "SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness":
        return self._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness(self)

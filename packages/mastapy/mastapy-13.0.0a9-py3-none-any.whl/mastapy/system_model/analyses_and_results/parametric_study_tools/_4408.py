"""SpecialisedAssemblyParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "SpecialisedAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyParametricStudyTool")


class SpecialisedAssemblyParametricStudyTool(_4292.AbstractAssemblyParametricStudyTool):
    """SpecialisedAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
            parent: "SpecialisedAssemblyParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            return self._parent._cast(_4292.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(
                _4298.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def belt_drive_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(_4302.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(
                _4367.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.RollingRingAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.ZerolBevelGearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
        ) -> "SpecialisedAssemblyParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyParametricStudyTool.TYPE"
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
    ) -> "SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool":
        return self._Cast_SpecialisedAssemblyParametricStudyTool(self)

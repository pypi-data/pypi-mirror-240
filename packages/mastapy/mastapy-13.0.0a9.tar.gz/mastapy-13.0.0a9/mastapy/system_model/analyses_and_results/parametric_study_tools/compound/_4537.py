"""SpecialisedAssemblyCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4439,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpecialisedAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4408


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundParametricStudyTool")


class SpecialisedAssemblyCompoundParametricStudyTool(
    _4439.AbstractAssemblyCompoundParametricStudyTool
):
    """SpecialisedAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundParametricStudyTool"
    )

    class _Cast_SpecialisedAssemblyCompoundParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
            parent: "SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4439.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(_4449.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(
                _4452.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(_4457.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(_4460.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConicalGearSetCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.CouplingCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CVTCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(
                _4482.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.FaceGearSetCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(
                _4496.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(
                _4507.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(
                _4530.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(_4541.SpringDamperCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(_4552.SynchroniserCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.TorqueConverterCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
        ) -> "SpecialisedAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4408.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4408.SpecialisedAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpecialisedAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundParametricStudyTool._Cast_SpecialisedAssemblyCompoundParametricStudyTool":
        return self._Cast_SpecialisedAssemblyCompoundParametricStudyTool(self)

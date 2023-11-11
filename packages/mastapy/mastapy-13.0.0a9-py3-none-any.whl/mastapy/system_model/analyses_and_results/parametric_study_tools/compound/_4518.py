"""PartCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "PartCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1847
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="PartCompoundParametricStudyTool")


class PartCompoundParametricStudyTool(_7542.PartCompoundAnalysis):
    """PartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundParametricStudyTool")

    class _Cast_PartCompoundParametricStudyTool:
        """Special nested class for casting PartCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
            parent: "PartCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4439,
            )

            return self._parent._cast(_4439.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4440,
            )

            return self._parent._cast(_4440.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4441,
            )

            return self._parent._cast(
                _4441.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(
                _4443.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(_4446.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(_4447.BearingCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(_4449.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(
                _4450.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(
                _4452.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(_4457.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(_4460.ClutchCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.ClutchHalfCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(_4470.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.CouplingCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(
                _4482.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(
                _4489.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(
                _4496.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.GearCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(
                _4507.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(_4514.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(_4523.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(_4525.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(
                _4530.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.RollingRingCompoundParametricStudyTool)

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(_4533.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(_4534.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(_4541.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(_4552.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(_4554.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(_4561.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(_4562.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_compound_parametric_study_tool(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
        ) -> "PartCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_logger(self: Self) -> "_1847.DataLoggerWithCharts":
        """mastapy.utility_gui.DataLoggerWithCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4389.PartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool]

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
    ) -> "List[_4389.PartParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.PartParametricStudyTool]

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
    ) -> "PartCompoundParametricStudyTool._Cast_PartCompoundParametricStudyTool":
        return self._Cast_PartCompoundParametricStudyTool(self)

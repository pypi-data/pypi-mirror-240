"""PartParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1856, _1864, _1862
    from mastapy.system_model.part_model import _2465
    from mastapy.utility_gui import _1847
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4384


__docformat__ = "restructuredtext en"
__all__ = ("PartParametricStudyTool",)


Self = TypeVar("Self", bound="PartParametricStudyTool")


class PartParametricStudyTool(_7541.PartAnalysisCase):
    """PartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartParametricStudyTool")

    class _Cast_PartParametricStudyTool:
        """Special nested class for casting PartParametricStudyTool to subclasses."""

        def __init__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
            parent: "PartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4292,
            )

            return self._parent._cast(_4292.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4293,
            )

            return self._parent._cast(_4293.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4294,
            )

            return self._parent._cast(_4294.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(
                _4298.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4299,
            )

            return self._parent._cast(_4299.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(_4302.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(
                _4306.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(_4312.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4333,
            )

            return self._parent._cast(_4333.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4351,
            )

            return self._parent._cast(_4351.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4356,
            )

            return self._parent._cast(_4356.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(
                _4366.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(
                _4367.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(_4374.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(_4377.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4394,
            )

            return self._parent._cast(_4394.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4406,
            )

            return self._parent._cast(_4406.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.ZerolBevelGearSetParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "PartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_of_experiments_chart(self: Self) -> "_1856.NDChartDefinition":
        """mastapy.utility_gui.charts.NDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignOfExperimentsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_2d(self: Self) -> "_1864.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart2D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_3d(self: Self) -> "_1862.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def parametric_study_tool(self: Self) -> "_4384.ParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartParametricStudyTool._Cast_PartParametricStudyTool":
        return self._Cast_PartParametricStudyTool(self)

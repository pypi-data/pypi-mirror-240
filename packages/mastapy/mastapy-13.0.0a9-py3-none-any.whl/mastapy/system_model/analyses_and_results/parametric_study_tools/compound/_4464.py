"""ComponentCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4518,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentCompoundParametricStudyTool")


class ComponentCompoundParametricStudyTool(_4518.PartCompoundParametricStudyTool):
    """ComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundParametricStudyTool")

    class _Cast_ComponentCompoundParametricStudyTool:
        """Special nested class for casting ComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
            parent: "ComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4518.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4440,
            )

            return self._parent._cast(_4440.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4441,
            )

            return self._parent._cast(
                _4441.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(
                _4443.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bearing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(_4447.BearingCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(
                _4450.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(
                _4453.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BevelGearCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(_4458.BoltCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConicalGearCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(
                _4489.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(_4491.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.FaceGearCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.FEPartCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.GearCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(
                _4505.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(_4514.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(_4525.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.RollingRingCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(_4534.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(_4543.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(
                _4547.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(_4554.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(_4561.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(_4562.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "ComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ComponentCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4317.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    ) -> "List[_4317.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    ) -> "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool":
        return self._Cast_ComponentCompoundParametricStudyTool(self)

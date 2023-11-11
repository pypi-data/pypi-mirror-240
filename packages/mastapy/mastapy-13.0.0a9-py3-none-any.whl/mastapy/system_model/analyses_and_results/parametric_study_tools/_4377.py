"""MountableComponentParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "MountableComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentParametricStudyTool",)


Self = TypeVar("Self", bound="MountableComponentParametricStudyTool")


class MountableComponentParametricStudyTool(_4317.ComponentParametricStudyTool):
    """MountableComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentParametricStudyTool"
    )

    class _Cast_MountableComponentParametricStudyTool:
        """Special nested class for casting MountableComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
            parent: "MountableComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            return self._parent._cast(_4317.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(
                _4306.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4307,
            )

            return self._parent._cast(_4307.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelGearParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CVTPulleyParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4342,
            )

            return self._parent._cast(_4342.CylindricalPlanetGearParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4353,
            )

            return self._parent._cast(_4353.FaceGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.GearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(
                _4366.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(
                _4369.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(_4374.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.MeasurementComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4391,
            )

            return self._parent._cast(
                _4391.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(_4397.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.ShaftHubConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4413,
            )

            return self._parent._cast(_4413.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.ZerolBevelGearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
        ) -> "MountableComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool",
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
        self: Self, instance_to_wrap: "MountableComponentParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentParametricStudyTool._Cast_MountableComponentParametricStudyTool":
        return self._Cast_MountableComponentParametricStudyTool(self)

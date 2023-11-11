"""AbstractAssemblyPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AbstractAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyPowerFlow",)


Self = TypeVar("Self", bound="AbstractAssemblyPowerFlow")


class AbstractAssemblyPowerFlow(_4110.PartPowerFlow):
    """AbstractAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyPowerFlow")

    class _Cast_AbstractAssemblyPowerFlow:
        """Special nested class for casting AbstractAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
            parent: "AbstractAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def part_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4036

            return self._parent._cast(_4036.AssemblyPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.CouplingPowerFlow)

        @property
        def cvt_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4079

            return self._parent._cast(_4079.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(
                _4102.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4115

            return self._parent._cast(_4115.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.RollingRingAssemblyPowerFlow)

        @property
        def root_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RootAssemblyPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow",
        ) -> "AbstractAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyPowerFlow.TYPE"):
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
    ) -> "AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow":
        return self._Cast_AbstractAssemblyPowerFlow(self)

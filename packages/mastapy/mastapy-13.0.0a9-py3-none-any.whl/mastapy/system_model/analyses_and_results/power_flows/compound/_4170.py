"""AssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2430
    from mastapy.gears.analysis import _1225
    from mastapy.system_model.analyses_and_results.power_flows import _4036
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4171,
        _4173,
        _4176,
        _4183,
        _4182,
        _4204,
        _4184,
        _4189,
        _4194,
        _4206,
        _4208,
        _4212,
        _4219,
        _4218,
        _4220,
        _4227,
        _4234,
        _4237,
        _4238,
        _4239,
        _4241,
        _4243,
        _4248,
        _4249,
        _4250,
        _4252,
        _4254,
        _4259,
        _4258,
        _4264,
        _4265,
        _4270,
        _4273,
        _4276,
        _4280,
        _4284,
        _4288,
        _4291,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="AssemblyCompoundPowerFlow")


class AssemblyCompoundPowerFlow(_4163.AbstractAssemblyCompoundPowerFlow):
    """AssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AssemblyCompoundPowerFlow")

    class _Cast_AssemblyCompoundPowerFlow:
        """Special nested class for casting AssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
            parent: "AssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_power_flow(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            return self._parent._cast(_4163.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def root_assembly_compound_power_flow(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.RootAssemblyCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow",
        ) -> "AssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AssemblyCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def input_power_load_ratio_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPowerLoadRatioWarning

        if temp is None:
            return ""

        return temp

    @property
    def output_power_load_ratio_warning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputPowerLoadRatioWarning

        if temp is None:
            return ""

        return temp

    @property
    def component_design(self: Self) -> "_2430.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2430.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_for_all_gear_sets(self: Self) -> "_1225.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingForAllGearSets

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(self: Self) -> "List[_4036.AssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow]

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
    def bearings(self: Self) -> "List[_4171.BearingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BearingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def belt_drives(self: Self) -> "List[_4173.BeltDriveCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BeltDriveCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltDrives

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gear_sets(
        self: Self,
    ) -> "List[_4176.BevelDifferentialGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolted_joints(self: Self) -> "List[_4183.BoltedJointCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BoltedJointCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoltedJoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolts(self: Self) -> "List[_4182.BoltCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BoltCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bolts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cv_ts(self: Self) -> "List[_4204.CVTCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CVTCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CVTs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def clutches(self: Self) -> "List[_4184.ClutchCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ClutchCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clutches

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_couplings(self: Self) -> "List[_4189.ConceptCouplingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptCouplingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gear_sets(self: Self) -> "List[_4194.ConceptGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_assemblies(
        self: Self,
    ) -> "List[_4206.CycloidalAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_discs(self: Self) -> "List[_4208.CycloidalDiscCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalDiscCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: Self,
    ) -> "List[_4212.CylindricalGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(self: Self) -> "List[_4219.FEPartCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FEPartCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_sets(self: Self) -> "List[_4218.FaceGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FaceGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_assemblies(
        self: Self,
    ) -> "List[_4220.FlexiblePinAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FlexiblePinAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_sets(self: Self) -> "List[_4227.HypoidGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(
        self: Self,
    ) -> "List[_4234.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(
        self: Self,
    ) -> "List[_4237.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_discs(self: Self) -> "List[_4238.MassDiscCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.MassDiscCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassDiscs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurement_components(
        self: Self,
    ) -> "List[_4239.MeasurementComponentCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.MeasurementComponentCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def oil_seals(self: Self) -> "List[_4241.OilSealCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.OilSealCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilSeals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def part_to_part_shear_couplings(
        self: Self,
    ) -> "List[_4243.PartToPartShearCouplingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PartToPartShearCouplingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_carriers(self: Self) -> "List[_4248.PlanetCarrierCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PlanetCarrierCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetCarriers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(self: Self) -> "List[_4249.PointLoadCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PointLoadCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(self: Self) -> "List[_4250.PowerLoadCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PowerLoadCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_pins(self: Self) -> "List[_4252.RingPinsCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.RingPinsCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPins

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_ring_assemblies(
        self: Self,
    ) -> "List[_4254.RollingRingAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.RollingRingAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingRingAssemblies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_hub_connections(
        self: Self,
    ) -> "List[_4259.ShaftHubConnectionCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftHubConnectionCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftHubConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts(self: Self) -> "List[_4258.ShaftCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shafts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gear_sets(
        self: Self,
    ) -> "List[_4264.SpiralBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dampers(self: Self) -> "List[_4265.SpringDamperCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpringDamperCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDampers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gear_sets(
        self: Self,
    ) -> "List[_4270.StraightBevelDiffGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gear_sets(
        self: Self,
    ) -> "List[_4273.StraightBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def synchronisers(self: Self) -> "List[_4276.SynchroniserCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Synchronisers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_converters(self: Self) -> "List[_4280.TorqueConverterCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unbalanced_masses(self: Self) -> "List[_4284.UnbalancedMassCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.UnbalancedMassCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnbalancedMasses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: Self) -> "List[_4288.WormGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gear_sets(
        self: Self,
    ) -> "List[_4291.ZerolBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4036.AssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow":
        return self._Cast_AssemblyCompoundPowerFlow(self)

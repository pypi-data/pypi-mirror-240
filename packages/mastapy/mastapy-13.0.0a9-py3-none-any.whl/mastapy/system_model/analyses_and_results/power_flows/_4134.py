"""SpiralBevelGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4047
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SpiralBevelGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6952
    from mastapy.gears.rating.spiral_bevel import _402
    from mastapy.system_model.analyses_and_results.power_flows import _4133, _4132


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearSetPowerFlow")


class SpiralBevelGearSetPowerFlow(_4047.BevelGearSetPowerFlow):
    """SpiralBevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetPowerFlow")

    class _Cast_SpiralBevelGearSetPowerFlow:
        """Special nested class for casting SpiralBevelGearSetPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
            parent: "SpiralBevelGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            return self._parent._cast(_4047.BevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4029

            return self._parent._cast(_4029.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
        ) -> "SpiralBevelGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2541.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6952.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_402.SpiralBevelGearSetRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_402.SpiralBevelGearSetRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4133.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_power_flow(
        self: Self,
    ) -> "List[_4133.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4132.SpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_power_flow(
        self: Self,
    ) -> "List[_4132.SpiralBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetPowerFlow._Cast_SpiralBevelGearSetPowerFlow":
        return self._Cast_SpiralBevelGearSetPowerFlow(self)

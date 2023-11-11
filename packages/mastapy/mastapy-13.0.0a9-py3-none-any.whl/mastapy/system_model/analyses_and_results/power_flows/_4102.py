"""KlingelnbergCycloPalloidHypoidGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4099
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6914
    from mastapy.gears.rating.klingelnberg_hypoid import _408
    from mastapy.system_model.analyses_and_results.power_flows import _4101, _4100


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetPowerFlow")


class KlingelnbergCycloPalloidHypoidGearSetPowerFlow(
    _4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4029

            return self._parent._cast(_4029.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6914.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_408.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_408.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(
        self: Self,
    ) -> "List[_4101.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_power_flow(
        self: Self,
    ) -> "List[_4101.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(
        self: Self,
    ) -> "List[_4100.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

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
    def klingelnberg_cyclo_palloid_hypoid_meshes_power_flow(
        self: Self,
    ) -> "List[_4100.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow(self)

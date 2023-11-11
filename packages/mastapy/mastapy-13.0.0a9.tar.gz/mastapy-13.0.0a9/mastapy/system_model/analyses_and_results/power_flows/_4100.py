"""KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_hypoid import _406
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.static_loads import _6913


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshPowerFlow")


class KlingelnbergCycloPalloidHypoidGearMeshPowerFlow(
    _4097.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            return self._parent._cast(
                _4097.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def conical_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4061

            return self._parent._cast(_4061.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_406.KlingelnbergCycloPalloidHypoidGearMeshRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshRating

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
    ) -> "_406.KlingelnbergCycloPalloidHypoidGearMeshRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2316.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshPowerFlow(self)

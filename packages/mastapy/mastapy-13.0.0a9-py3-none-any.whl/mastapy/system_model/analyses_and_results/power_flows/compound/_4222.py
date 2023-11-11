"""GearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _363
    from mastapy.system_model.analyses_and_results.power_flows import _4089


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearMeshCompoundPowerFlow")


class GearMeshCompoundPowerFlow(
    _4228.InterMountableComponentConnectionCompoundPowerFlow
):
    """GearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundPowerFlow")

    class _Cast_GearMeshCompoundPowerFlow:
        """Special nested class for casting GearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
            parent: "GearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            return self._parent._cast(
                _4228.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelGearMeshCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConicalGearMeshCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.FaceGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(
                _4230.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow",
        ) -> "GearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_rating(self: Self) -> "_363.MeshDutyCycleRating":
        """mastapy.gears.rating.MeshDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases(self: Self) -> "List[_4089.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(self: Self) -> "List[_4089.GearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow":
        return self._Cast_GearMeshCompoundPowerFlow(self)

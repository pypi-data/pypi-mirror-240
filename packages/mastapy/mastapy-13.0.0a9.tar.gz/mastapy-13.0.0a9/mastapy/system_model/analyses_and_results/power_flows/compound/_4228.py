"""InterMountableComponentConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "InterMountableComponentConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4096


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundPowerFlow")


class InterMountableComponentConnectionCompoundPowerFlow(
    _4198.ConnectionCompoundPowerFlow
):
    """InterMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionCompoundPowerFlow"
    )

    class _Cast_InterMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting InterMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
            parent: "InterMountableComponentConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(_4198.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4172,
            )

            return self._parent._cast(_4172.BeltConnectionCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelGearMeshCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConicalGearMeshCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.FaceGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.GearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(
                _4230.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(
                _4244.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.RollingRingConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.SpringDamperConnectionCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
        ) -> "InterMountableComponentConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4096.InterMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4096.InterMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow]

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
    ) -> "InterMountableComponentConnectionCompoundPowerFlow._Cast_InterMountableComponentConnectionCompoundPowerFlow":
        return self._Cast_InterMountableComponentConnectionCompoundPowerFlow(self)

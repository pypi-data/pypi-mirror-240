"""ConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectionCriticalSpeedAnalysis")


class ConnectionCriticalSpeedAnalysis(_7537.ConnectionStaticLoadAnalysisCase):
    """ConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCriticalSpeedAnalysis")

    class _Cast_ConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
            parent: "ConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(
                _6542.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(
                _6544.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def belt_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6548,
            )

            return self._parent._cast(_6548.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(
                _6551.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(_6563.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(
                _6565.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6576,
            )

            return self._parent._cast(_6576.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(
                _6586.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(
                _6588.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(
                _6609.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(
                _6612.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(
                _6615.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(
                _6632.RingPinsToDiscConnectionCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(
                _6639.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(
                _6648.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(
                _6659.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
        ) -> "ConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2269.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2269.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis(self: Self) -> "_6579.CriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis":
        return self._Cast_ConnectionCriticalSpeedAnalysis(self)

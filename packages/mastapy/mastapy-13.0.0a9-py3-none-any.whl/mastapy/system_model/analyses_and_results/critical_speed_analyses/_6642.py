"""SpiralBevelGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320
    from mastapy.system_model.analyses_and_results.static_loads import _6951


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCriticalSpeedAnalysis")


class SpiralBevelGearMeshCriticalSpeedAnalysis(
    _6556.BevelGearMeshCriticalSpeedAnalysis
):
    """SpiralBevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCriticalSpeedAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
            parent: "SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6556.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(
                _6544.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2320.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6951.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

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
    ) -> "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis(self)

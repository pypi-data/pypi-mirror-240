"""FaceGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "FaceGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.static_loads import _6882


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshCriticalSpeedAnalysis")


class FaceGearMeshCriticalSpeedAnalysis(_6601.GearMeshCriticalSpeedAnalysis):
    """FaceGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshCriticalSpeedAnalysis")

    class _Cast_FaceGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting FaceGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
            parent: "FaceGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6601.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
        ) -> "FaceGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2308.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6882.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshCriticalSpeedAnalysis._Cast_FaceGearMeshCriticalSpeedAnalysis":
        return self._Cast_FaceGearMeshCriticalSpeedAnalysis(self)

"""HypoidGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "HypoidGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6903


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="HypoidGearMeshMultibodyDynamicsAnalysis")


class HypoidGearMeshMultibodyDynamicsAnalysis(
    _5376.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
):
    """HypoidGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_HypoidGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting HypoidGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
            parent: "HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5376.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(
                _5445.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
        ) -> "HypoidGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6903.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshMultibodyDynamicsAnalysis._Cast_HypoidGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_HypoidGearMeshMultibodyDynamicsAnalysis(self)

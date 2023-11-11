"""StraightBevelGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2324
    from mastapy.system_model.analyses_and_results.static_loads import _6960


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshMultibodyDynamicsAnalysis")


class StraightBevelGearMeshMultibodyDynamicsAnalysis(
    _5390.BevelGearMeshMultibodyDynamicsAnalysis
):
    """StraightBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5390.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(
                _5376.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(
                _5445.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "StraightBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2324.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6960.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

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
    ) -> "StraightBevelGearMeshMultibodyDynamicsAnalysis._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelGearMeshMultibodyDynamicsAnalysis(self)

"""AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(
    _5407.ConicalGearMeshMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5407.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(
                _5445.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(
                _5385.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(_5390.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2296.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(self)

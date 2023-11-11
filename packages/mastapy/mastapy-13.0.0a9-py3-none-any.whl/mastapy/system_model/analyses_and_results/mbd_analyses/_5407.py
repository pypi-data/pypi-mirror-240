"""ConicalGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5433
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2304


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshMultibodyDynamicsAnalysis")


class ConicalGearMeshMultibodyDynamicsAnalysis(_5433.GearMeshMultibodyDynamicsAnalysis):
    """ConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_ConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5433.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(
                _5445.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(
                _5376.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(
                _5385.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(_5390.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(
                _5486.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "ConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2304.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearMeshMultibodyDynamicsAnalysis(self)

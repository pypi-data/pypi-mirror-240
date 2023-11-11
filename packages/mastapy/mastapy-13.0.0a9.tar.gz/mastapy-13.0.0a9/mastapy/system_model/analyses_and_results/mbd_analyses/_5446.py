"""KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis(
    _5407.ConicalGearMeshMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5407.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(
                _5445.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2315.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis(
                self
            )
        )

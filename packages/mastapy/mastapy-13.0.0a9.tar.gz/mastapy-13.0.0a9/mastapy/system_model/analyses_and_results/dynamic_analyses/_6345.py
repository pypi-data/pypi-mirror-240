"""KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.static_loads import _6913


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis")


class KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis(
    _6342.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(
                _6342.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(
                _6340.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2316.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis(self)

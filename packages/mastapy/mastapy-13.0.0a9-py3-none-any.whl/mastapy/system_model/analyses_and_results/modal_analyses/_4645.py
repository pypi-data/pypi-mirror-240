"""KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4639
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.system_deflections import _2771


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis")


class KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis(
    _4639.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            return self._parent._cast(
                _4639.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def conical_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(
                _4638.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2317.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

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
    ) -> "_6916.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2771.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis(self)

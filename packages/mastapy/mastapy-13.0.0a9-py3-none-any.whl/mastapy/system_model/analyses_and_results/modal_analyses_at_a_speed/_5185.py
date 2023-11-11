"""KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.static_loads import _6916


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed(
    _5179.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5179.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(
                _5178.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed(
                self
            )
        )

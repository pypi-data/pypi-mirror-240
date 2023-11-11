"""BevelGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2300
    from mastapy.system_model.analyses_and_results.system_deflections import _2703


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysis")


class BevelGearMeshModalAnalysis(_4572.AGMAGleasonConicalGearMeshModalAnalysis):
    """BevelGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshModalAnalysis")

    class _Cast_BevelGearMeshModalAnalysis:
        """Special nested class for casting BevelGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
            parent: "BevelGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            return self._parent._cast(_4572.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(
                _4638.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.BevelDifferentialGearMeshModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.StraightBevelGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.ZerolBevelGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
        ) -> "BevelGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2300.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2703.BevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection

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
    ) -> "BevelGearMeshModalAnalysis._Cast_BevelGearMeshModalAnalysis":
        return self._Cast_BevelGearMeshModalAnalysis(self)

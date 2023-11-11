"""StraightBevelDiffGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelDiffGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshStabilityAnalysis")


class StraightBevelDiffGearMeshStabilityAnalysis(_3776.BevelGearMeshStabilityAnalysis):
    """StraightBevelDiffGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
            parent: "StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            return self._parent._cast(_3776.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(_3764.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(
                _3827.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "StraightBevelDiffGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

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
    ) -> "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearMeshStabilityAnalysis(self)

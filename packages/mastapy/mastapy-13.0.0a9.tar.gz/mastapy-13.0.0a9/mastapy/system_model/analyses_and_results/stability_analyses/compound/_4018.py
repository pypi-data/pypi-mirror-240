"""WormGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "WormGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.stability_analyses import _3888


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshCompoundStabilityAnalysis")


class WormGearMeshCompoundStabilityAnalysis(_3953.GearMeshCompoundStabilityAnalysis):
    """WormGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_WormGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting WormGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
            parent: "WormGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_stability_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3953.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(
                _3959.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
        ) -> "WormGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2326.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2326.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3888.WormGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3888.WormGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.WormGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshCompoundStabilityAnalysis._Cast_WormGearMeshCompoundStabilityAnalysis":
        return self._Cast_WormGearMeshCompoundStabilityAnalysis(self)

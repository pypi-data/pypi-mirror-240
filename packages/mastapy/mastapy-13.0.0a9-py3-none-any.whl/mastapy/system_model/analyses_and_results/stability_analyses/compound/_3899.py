"""AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3764


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundStabilityAnalysis")


class AGMAGleasonConicalGearMeshCompoundStabilityAnalysis(
    _3927.ConicalGearMeshCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3927.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(
                _3959.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3764.AGMAGleasonConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearMeshStabilityAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3764.AGMAGleasonConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearMeshStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundStabilityAnalysis(self)

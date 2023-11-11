"""AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6704,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis")


class AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(
    _6704.ConicalGearMeshCompoundCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6704.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(
                _6736.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(_6688.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(
                _6771.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(
                _6798.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6544.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6544.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(self)

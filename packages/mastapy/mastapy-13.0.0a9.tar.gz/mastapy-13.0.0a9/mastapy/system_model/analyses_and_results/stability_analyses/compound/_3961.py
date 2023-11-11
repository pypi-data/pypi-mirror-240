"""KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3828


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis(
    _3927.ConicalGearMeshCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3927.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(
                _3959.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3828.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]

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
    ) -> "List[_3828.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis(
                self
            )
        )

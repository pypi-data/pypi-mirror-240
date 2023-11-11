"""ConnectorCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6748,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConnectorCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundCriticalSpeedAnalysis")


class ConnectorCompoundCriticalSpeedAnalysis(
    _6748.MountableComponentCompoundCriticalSpeedAnalysis
):
    """ConnectorCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ConnectorCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConnectorCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
            parent: "ConnectorCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(_6679.BearingCompoundCriticalSpeedAnalysis)

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(_6749.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(
                _6767.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connector_compound_critical_speed_analysis(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
        ) -> "ConnectorCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6575.ConnectorCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConnectorCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6575.ConnectorCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConnectorCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis":
        return self._Cast_ConnectorCompoundCriticalSpeedAnalysis(self)

"""ConnectorCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6481
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConnectorCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundDynamicAnalysis")


class ConnectorCompoundDynamicAnalysis(_6481.MountableComponentCompoundDynamicAnalysis):
    """ConnectorCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundDynamicAnalysis")

    class _Cast_ConnectorCompoundDynamicAnalysis:
        """Special nested class for casting ConnectorCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
            parent: "ConnectorCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6481.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(_6412.BearingCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.OilSealCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "ConnectorCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6309.ConnectorDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis]

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
    ) -> "List[_6309.ConnectorDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis]

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
    ) -> "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis":
        return self._Cast_ConnectorCompoundDynamicAnalysis(self)

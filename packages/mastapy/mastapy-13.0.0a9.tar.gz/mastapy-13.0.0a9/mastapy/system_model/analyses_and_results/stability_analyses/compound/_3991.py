"""ShaftToMountableComponentConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3897
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3859


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundStabilityAnalysis"
)


class ShaftToMountableComponentConnectionCompoundStabilityAnalysis(
    _3897.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """ShaftToMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3897.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(
                _3938.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3859.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "List[_3859.ShaftToMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftToMountableComponentConnectionStabilityAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundStabilityAnalysis._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundStabilityAnalysis(
            self
        )

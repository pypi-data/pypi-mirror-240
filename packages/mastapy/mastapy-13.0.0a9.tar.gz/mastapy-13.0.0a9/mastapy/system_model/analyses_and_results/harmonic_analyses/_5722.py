"""CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6857
    from mastapy.system_model.analyses_and_results.system_deflections import _2734


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis")


class CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis(
    _5678.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5678.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2335.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

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
    ) -> "_6857.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2734.CycloidalDiscPlanetaryBearingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscPlanetaryBearingConnectionSystemDeflection

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis(self)

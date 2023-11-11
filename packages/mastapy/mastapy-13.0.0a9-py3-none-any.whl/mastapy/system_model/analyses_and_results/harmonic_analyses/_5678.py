"""AbstractShaftToMountableComponentConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262
    from mastapy.system_model.analyses_and_results.system_deflections import _2685


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionHarmonicAnalysis"
)


class AbstractShaftToMountableComponentConnectionHarmonicAnalysis(
    _5711.ConnectionHarmonicAnalysis
):
    """AbstractShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(
                _5720.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(
                _5722.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
            )

        @property
        def planetary_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(_5789.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(
                _5804.ShaftToMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2262.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2685.AbstractShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftToMountableComponentConnectionSystemDeflection

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
    ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis(
            self
        )

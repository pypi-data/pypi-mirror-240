"""AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6039,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
)


class AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6039.ConnectionHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6039.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(
                _6028.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(
                _6050.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.PlanetaryConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )

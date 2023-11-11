"""ConceptCouplingConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConceptCouplingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6835
    from mastapy.system_model.analyses_and_results.system_deflections import _2714


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionHarmonicAnalysis")


class ConceptCouplingConnectionHarmonicAnalysis(
    _5713.CouplingConnectionHarmonicAnalysis
):
    """ConceptCouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionHarmonicAnalysis"
    )

    class _Cast_ConceptCouplingConnectionHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
            parent: "ConceptCouplingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5713.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(
                _5770.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ) -> "ConceptCouplingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2341.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6835.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

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
    ) -> "_2714.ConceptCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection

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
    ) -> "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis":
        return self._Cast_ConceptCouplingConnectionHarmonicAnalysis(self)

"""CouplingConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343
    from mastapy.system_model.analyses_and_results.system_deflections import _2726


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionHarmonicAnalysis")


class CouplingConnectionHarmonicAnalysis(
    _5770.InterMountableComponentConnectionHarmonicAnalysis
):
    """CouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionHarmonicAnalysis")

    class _Cast_CouplingConnectionHarmonicAnalysis:
        """Special nested class for casting CouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
            parent: "CouplingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5770.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.ClutchConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(
                _5785.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.SpringDamperConnectionHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
        ) -> "CouplingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "_2726.CouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection

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
    ) -> "CouplingConnectionHarmonicAnalysis._Cast_CouplingConnectionHarmonicAnalysis":
        return self._Cast_CouplingConnectionHarmonicAnalysis(self)

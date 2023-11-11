"""PartToPartShearCouplingConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2345
    from mastapy.system_model.analyses_and_results.static_loads import _6926
    from mastapy.system_model.analyses_and_results.system_deflections import _2783


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionHarmonicAnalysis")


class PartToPartShearCouplingConnectionHarmonicAnalysis(
    _5713.CouplingConnectionHarmonicAnalysis
):
    """PartToPartShearCouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionHarmonicAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionHarmonicAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
            parent: "PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5713.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(
                _5770.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
        ) -> "PartToPartShearCouplingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2345.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "_6926.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

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
    ) -> "_2783.PartToPartShearCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection

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
    ) -> "PartToPartShearCouplingConnectionHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionHarmonicAnalysis(self)

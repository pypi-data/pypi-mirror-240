"""TorqueConverterTurbineHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "TorqueConverterTurbineHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.system_deflections import _2828


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineHarmonicAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineHarmonicAnalysis")


class TorqueConverterTurbineHarmonicAnalysis(_5714.CouplingHalfHarmonicAnalysis):
    """TorqueConverterTurbineHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineHarmonicAnalysis"
    )

    class _Cast_TorqueConverterTurbineHarmonicAnalysis:
        """Special nested class for casting TorqueConverterTurbineHarmonicAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
            parent: "TorqueConverterTurbineHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            return self._parent._cast(_5714.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
        ) -> "TorqueConverterTurbineHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6972.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2828.TorqueConverterTurbineSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection

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
    ) -> "TorqueConverterTurbineHarmonicAnalysis._Cast_TorqueConverterTurbineHarmonicAnalysis":
        return self._Cast_TorqueConverterTurbineHarmonicAnalysis(self)

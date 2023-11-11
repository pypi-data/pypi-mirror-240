"""TorqueConverterHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6043,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "TorqueConverterHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6970


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="TorqueConverterHarmonicAnalysisOfSingleExcitation")


class TorqueConverterHarmonicAnalysisOfSingleExcitation(
    _6043.CouplingHarmonicAnalysisOfSingleExcitation
):
    """TorqueConverterHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting TorqueConverterHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
            parent: "TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6043.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6004,
            )

            return self._parent._cast(
                _6004.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
        ) -> "TorqueConverterHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "TorqueConverterHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6970.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterHarmonicAnalysisOfSingleExcitation._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation":
        return self._Cast_TorqueConverterHarmonicAnalysisOfSingleExcitation(self)

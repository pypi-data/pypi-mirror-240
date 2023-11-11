"""ConceptGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6062,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.static_loads import _6838


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptGearHarmonicAnalysisOfSingleExcitation")


class ConceptGearHarmonicAnalysisOfSingleExcitation(
    _6062.GearHarmonicAnalysisOfSingleExcitation
):
    """ConceptGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6062.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2518.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6838.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptGearHarmonicAnalysisOfSingleExcitation(self)

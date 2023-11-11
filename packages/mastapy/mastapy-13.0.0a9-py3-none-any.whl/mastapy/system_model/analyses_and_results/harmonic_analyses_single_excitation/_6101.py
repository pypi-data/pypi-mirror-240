"""ShaftHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6005,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ShaftHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2479
    from mastapy.system_model.analyses_and_results.static_loads import _6947


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ShaftHarmonicAnalysisOfSingleExcitation")


class ShaftHarmonicAnalysisOfSingleExcitation(
    _6005.AbstractShaftHarmonicAnalysisOfSingleExcitation
):
    """ShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ShaftHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6005.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6006,
            )

            return self._parent._cast(
                _6006.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "ShaftHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6947.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftHarmonicAnalysisOfSingleExcitation(self)

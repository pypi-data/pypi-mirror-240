"""RingPinsHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6083,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "RingPinsHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.static_loads import _6940


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="RingPinsHarmonicAnalysisOfSingleExcitation")


class RingPinsHarmonicAnalysisOfSingleExcitation(
    _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """RingPinsHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_RingPinsHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RingPinsHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
            parent: "RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
        ) -> "RingPinsHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "RingPinsHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6940.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

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
    ) -> "RingPinsHarmonicAnalysisOfSingleExcitation._Cast_RingPinsHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RingPinsHarmonicAnalysisOfSingleExcitation(self)

"""HypoidGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6008,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "HypoidGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.static_loads import _6902


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="HypoidGearHarmonicAnalysisOfSingleExcitation")


class HypoidGearHarmonicAnalysisOfSingleExcitation(
    _6008.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
):
    """HypoidGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_HypoidGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting HypoidGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
            parent: "HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6008.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(_6062.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
        ) -> "HypoidGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "HypoidGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6902.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

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
    ) -> "HypoidGearHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_HypoidGearHarmonicAnalysisOfSingleExcitation(self)

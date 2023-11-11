"""AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6029,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation")


class AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation(
    _6029.ComponentHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(
                _6049.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(_6060.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(_6101.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation(self)

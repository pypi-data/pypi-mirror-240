"""CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6212,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6042,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation")


class CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(
    _6212.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6212.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6250,
            )

            return self._parent._cast(
                _6250.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6042.CouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHalfHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6042.CouplingHalfHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHalfHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation(self)

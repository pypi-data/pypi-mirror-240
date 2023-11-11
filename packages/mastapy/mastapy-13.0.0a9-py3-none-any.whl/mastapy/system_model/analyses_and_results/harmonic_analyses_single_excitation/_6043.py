"""CouplingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6104,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CouplingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingHarmonicAnalysisOfSingleExcitation")


class CouplingHarmonicAnalysisOfSingleExcitation(
    _6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
):
    """CouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6104.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6004,
            )

            return self._parent._cast(
                _6004.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(_6027.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(
                _6088.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "CouplingHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHarmonicAnalysisOfSingleExcitation._Cast_CouplingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingHarmonicAnalysisOfSingleExcitation(self)

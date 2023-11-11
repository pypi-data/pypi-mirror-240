"""ConceptGearMeshHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6063,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2302
    from mastapy.system_model.analyses_and_results.static_loads import _6839


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ConceptGearMeshHarmonicAnalysisOfSingleExcitation")


class ConceptGearMeshHarmonicAnalysisOfSingleExcitation(
    _6063.GearMeshHarmonicAnalysisOfSingleExcitation
):
    """ConceptGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConceptGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6063.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6070,
            )

            return self._parent._cast(
                _6070.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ConceptGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2302.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6839.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshHarmonicAnalysisOfSingleExcitation._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ConceptGearMeshHarmonicAnalysisOfSingleExcitation(self)

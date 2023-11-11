"""VirtualComponentHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6083,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "VirtualComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="VirtualComponentHarmonicAnalysisOfSingleExcitation")


class VirtualComponentHarmonicAnalysisOfSingleExcitation(
    _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6083.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6029,
            )

            return self._parent._cast(_6029.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(_6085.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(_6080.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(_6092.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(_6093.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2476.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentHarmonicAnalysisOfSingleExcitation(self)

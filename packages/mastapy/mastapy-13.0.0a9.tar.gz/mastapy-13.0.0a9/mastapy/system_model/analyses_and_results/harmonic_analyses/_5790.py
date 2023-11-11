"""PlanetaryGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5725
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PlanetaryGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetHarmonicAnalysis")


class PlanetaryGearSetHarmonicAnalysis(_5725.CylindricalGearSetHarmonicAnalysis):
    """PlanetaryGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetHarmonicAnalysis")

    class _Cast_PlanetaryGearSetHarmonicAnalysis:
        """Special nested class for casting PlanetaryGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
            parent: "PlanetaryGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5725.CylindricalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
        ) -> "PlanetaryGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetHarmonicAnalysis._Cast_PlanetaryGearSetHarmonicAnalysis":
        return self._Cast_PlanetaryGearSetHarmonicAnalysis(self)

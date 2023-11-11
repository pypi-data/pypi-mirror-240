"""AGMAGleasonConicalGearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.system_deflections import _2687


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetHarmonicAnalysis")


class AGMAGleasonConicalGearSetHarmonicAnalysis(_5710.ConicalGearSetHarmonicAnalysis):
    """AGMAGleasonConicalGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5710.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5754,
            )

            return self._parent._cast(_5754.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5674,
            )

            return self._parent._cast(_5674.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearSetHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2687.AGMAGleasonConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetHarmonicAnalysis(self)

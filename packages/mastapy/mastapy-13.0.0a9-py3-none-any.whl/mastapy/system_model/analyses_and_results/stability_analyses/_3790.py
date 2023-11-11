"""ConceptGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConceptGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3791,
        _3789,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetStabilityAnalysis")


class ConceptGearSetStabilityAnalysis(_3821.GearSetStabilityAnalysis):
    """ConceptGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetStabilityAnalysis")

    class _Cast_ConceptGearSetStabilityAnalysis:
        """Special nested class for casting ConceptGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
            parent: "ConceptGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
        ) -> "ConceptGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2519.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6840.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_stability_analysis(
        self: Self,
    ) -> "List[_3791.ConceptGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3789.ConceptGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConceptGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetStabilityAnalysis._Cast_ConceptGearSetStabilityAnalysis":
        return self._Cast_ConceptGearSetStabilityAnalysis(self)

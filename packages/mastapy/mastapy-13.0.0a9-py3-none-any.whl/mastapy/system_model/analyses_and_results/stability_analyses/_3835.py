"""KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
        "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3836,
        _3834,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis(
    _3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2538.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6917.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_stability_analysis(
        self: Self,
    ) -> "List[_3836.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3834.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis(
            self
        )

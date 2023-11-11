"""KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis")


class KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis(
    _3793.ConicalGearSetStabilityAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3793.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis(self)

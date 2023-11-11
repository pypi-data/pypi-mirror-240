"""RollingRingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3798
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RollingRingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2593
    from mastapy.system_model.analyses_and_results.static_loads import _6944


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingStabilityAnalysis",)


Self = TypeVar("Self", bound="RollingRingStabilityAnalysis")


class RollingRingStabilityAnalysis(_3798.CouplingHalfStabilityAnalysis):
    """RollingRingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingStabilityAnalysis")

    class _Cast_RollingRingStabilityAnalysis:
        """Special nested class for casting RollingRingStabilityAnalysis to subclasses."""

        def __init__(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
            parent: "RollingRingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            return self._parent._cast(_3798.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ) -> "RollingRingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2593.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6944.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RollingRingStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis":
        return self._Cast_RollingRingStabilityAnalysis(self)

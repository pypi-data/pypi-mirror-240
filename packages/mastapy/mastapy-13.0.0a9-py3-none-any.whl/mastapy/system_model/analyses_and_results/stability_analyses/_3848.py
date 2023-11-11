"""PointLoadStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3887
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PointLoadStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6935


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadStabilityAnalysis",)


Self = TypeVar("Self", bound="PointLoadStabilityAnalysis")


class PointLoadStabilityAnalysis(_3887.VirtualComponentStabilityAnalysis):
    """PointLoadStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadStabilityAnalysis")

    class _Cast_PointLoadStabilityAnalysis:
        """Special nested class for casting PointLoadStabilityAnalysis to subclasses."""

        def __init__(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
            parent: "PointLoadStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_stability_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            return self._parent._cast(_3887.VirtualComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
        ) -> "PointLoadStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2468.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6935.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PointLoadStabilityAnalysis._Cast_PointLoadStabilityAnalysis":
        return self._Cast_PointLoadStabilityAnalysis(self)

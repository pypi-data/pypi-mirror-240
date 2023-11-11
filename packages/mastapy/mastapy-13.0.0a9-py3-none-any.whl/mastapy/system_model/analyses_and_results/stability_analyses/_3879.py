"""SynchroniserPartStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3798
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SynchroniserPartStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartStabilityAnalysis")


class SynchroniserPartStabilityAnalysis(_3798.CouplingHalfStabilityAnalysis):
    """SynchroniserPartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartStabilityAnalysis")

    class _Cast_SynchroniserPartStabilityAnalysis:
        """Special nested class for casting SynchroniserPartStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
            parent: "SynchroniserPartStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            return self._parent._cast(_3798.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ) -> "SynchroniserPartStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis":
        return self._Cast_SynchroniserPartStabilityAnalysis(self)

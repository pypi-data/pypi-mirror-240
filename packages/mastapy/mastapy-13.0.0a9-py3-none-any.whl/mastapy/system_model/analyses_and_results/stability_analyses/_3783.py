"""ClutchStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ClutchStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.static_loads import _6831


__docformat__ = "restructuredtext en"
__all__ = ("ClutchStabilityAnalysis",)


Self = TypeVar("Self", bound="ClutchStabilityAnalysis")


class ClutchStabilityAnalysis(_3799.CouplingStabilityAnalysis):
    """ClutchStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchStabilityAnalysis")

    class _Cast_ClutchStabilityAnalysis:
        """Special nested class for casting ClutchStabilityAnalysis to subclasses."""

        def __init__(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
            parent: "ClutchStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            return self._parent._cast(_3799.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis",
        ) -> "ClutchStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6831.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchStabilityAnalysis._Cast_ClutchStabilityAnalysis":
        return self._Cast_ClutchStabilityAnalysis(self)

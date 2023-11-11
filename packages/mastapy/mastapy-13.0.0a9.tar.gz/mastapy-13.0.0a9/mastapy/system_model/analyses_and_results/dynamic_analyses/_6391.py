"""SynchroniserSleeveDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserSleeveDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.static_loads import _6967


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveDynamicAnalysis")


class SynchroniserSleeveDynamicAnalysis(_6390.SynchroniserPartDynamicAnalysis):
    """SynchroniserSleeveDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveDynamicAnalysis")

    class _Cast_SynchroniserSleeveDynamicAnalysis:
        """Special nested class for casting SynchroniserSleeveDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
            parent: "SynchroniserSleeveDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            return self._parent._cast(_6390.SynchroniserPartDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
        ) -> "SynchroniserSleeveDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6967.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "SynchroniserSleeveDynamicAnalysis._Cast_SynchroniserSleeveDynamicAnalysis":
        return self._Cast_SynchroniserSleeveDynamicAnalysis(self)

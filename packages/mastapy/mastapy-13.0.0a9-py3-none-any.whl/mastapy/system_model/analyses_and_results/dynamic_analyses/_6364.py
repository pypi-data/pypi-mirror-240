"""RingPinsDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "RingPinsDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.static_loads import _6940


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsDynamicAnalysis",)


Self = TypeVar("Self", bound="RingPinsDynamicAnalysis")


class RingPinsDynamicAnalysis(_6352.MountableComponentDynamicAnalysis):
    """RingPinsDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsDynamicAnalysis")

    class _Cast_RingPinsDynamicAnalysis:
        """Special nested class for casting RingPinsDynamicAnalysis to subclasses."""

        def __init__(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
            parent: "RingPinsDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis",
        ) -> "RingPinsDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6940.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsDynamicAnalysis._Cast_RingPinsDynamicAnalysis":
        return self._Cast_RingPinsDynamicAnalysis(self)

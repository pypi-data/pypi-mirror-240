"""ShaftHubConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ShaftHubConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.static_loads import _6946


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionDynamicAnalysis")


class ShaftHubConnectionDynamicAnalysis(_6309.ConnectorDynamicAnalysis):
    """ShaftHubConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionDynamicAnalysis")

    class _Cast_ShaftHubConnectionDynamicAnalysis:
        """Special nested class for casting ShaftHubConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
            parent: "ShaftHubConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_dynamic_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            return self._parent._cast(_6309.ConnectorDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
        ) -> "ShaftHubConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2595.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6946.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftHubConnectionDynamicAnalysis]

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
    ) -> "ShaftHubConnectionDynamicAnalysis._Cast_ShaftHubConnectionDynamicAnalysis":
        return self._Cast_ShaftHubConnectionDynamicAnalysis(self)

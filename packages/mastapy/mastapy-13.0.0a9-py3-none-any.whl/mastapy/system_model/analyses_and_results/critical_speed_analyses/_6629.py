"""PowerLoadCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PowerLoadCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6936


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCriticalSpeedAnalysis")


class PowerLoadCriticalSpeedAnalysis(_6664.VirtualComponentCriticalSpeedAnalysis):
    """PowerLoadCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCriticalSpeedAnalysis")

    class _Cast_PowerLoadCriticalSpeedAnalysis:
        """Special nested class for casting PowerLoadCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
            parent: "PowerLoadCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6664.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ) -> "PowerLoadCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6936.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis":
        return self._Cast_PowerLoadCriticalSpeedAnalysis(self)

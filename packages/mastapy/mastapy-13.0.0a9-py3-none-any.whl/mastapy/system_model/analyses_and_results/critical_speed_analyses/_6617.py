"""MassDiscCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "MassDiscCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6918


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="MassDiscCriticalSpeedAnalysis")


class MassDiscCriticalSpeedAnalysis(_6664.VirtualComponentCriticalSpeedAnalysis):
    """MassDiscCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCriticalSpeedAnalysis")

    class _Cast_MassDiscCriticalSpeedAnalysis:
        """Special nested class for casting MassDiscCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
            parent: "MassDiscCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6664.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_critical_speed_analysis(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
        ) -> "MassDiscCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6918.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.MassDiscCriticalSpeedAnalysis]

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
    ) -> "MassDiscCriticalSpeedAnalysis._Cast_MassDiscCriticalSpeedAnalysis":
        return self._Cast_MassDiscCriticalSpeedAnalysis(self)

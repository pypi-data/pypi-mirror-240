"""SynchroniserPartCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SynchroniserPartCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCriticalSpeedAnalysis")


class SynchroniserPartCriticalSpeedAnalysis(_6578.CouplingHalfCriticalSpeedAnalysis):
    """SynchroniserPartCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserPartCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserPartCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
            parent: "SynchroniserPartCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6578.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6619,
            )

            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
        ) -> "SynchroniserPartCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCriticalSpeedAnalysis.TYPE"
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
    ) -> "SynchroniserPartCriticalSpeedAnalysis._Cast_SynchroniserPartCriticalSpeedAnalysis":
        return self._Cast_SynchroniserPartCriticalSpeedAnalysis(self)

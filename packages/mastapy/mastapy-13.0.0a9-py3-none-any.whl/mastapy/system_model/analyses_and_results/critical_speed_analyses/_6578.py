"""CouplingHalfCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CouplingHalfCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCriticalSpeedAnalysis")


class CouplingHalfCriticalSpeedAnalysis(_6619.MountableComponentCriticalSpeedAnalysis):
    """CouplingHalfCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCriticalSpeedAnalysis")

    class _Cast_CouplingHalfCriticalSpeedAnalysis:
        """Special nested class for casting CouplingHalfCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
            parent: "CouplingHalfCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6619.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CVTPulleyCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(
                _6624.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def pulley_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PulleyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RollingRingCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
        ) -> "CouplingHalfCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfCriticalSpeedAnalysis._Cast_CouplingHalfCriticalSpeedAnalysis":
        return self._Cast_CouplingHalfCriticalSpeedAnalysis(self)

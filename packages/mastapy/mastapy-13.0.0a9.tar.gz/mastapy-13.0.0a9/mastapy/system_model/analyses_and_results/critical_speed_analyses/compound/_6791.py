"""TorqueConverterTurbineCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6710,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6662


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundCriticalSpeedAnalysis")


class TorqueConverterTurbineCompoundCriticalSpeedAnalysis(
    _6710.CouplingHalfCompoundCriticalSpeedAnalysis
):
    """TorqueConverterTurbineCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis"
    )

    class _Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
            parent: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6710.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
        ) -> "TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "TorqueConverterTurbineCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6662.TorqueConverterTurbineCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.TorqueConverterTurbineCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6662.TorqueConverterTurbineCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.TorqueConverterTurbineCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineCompoundCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundCriticalSpeedAnalysis(self)

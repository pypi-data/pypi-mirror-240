"""CouplingHalfCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6748,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundCriticalSpeedAnalysis")


class CouplingHalfCompoundCriticalSpeedAnalysis(
    _6748.MountableComponentCompoundCriticalSpeedAnalysis
):
    """CouplingHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CouplingHalfCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingHalfCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
            parent: "CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6748.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(_6713.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(
                _6753.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def pulley_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(_6759.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
        ) -> "CouplingHalfCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6578.CouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingHalfCriticalSpeedAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6578.CouplingHalfCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingHalfCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundCriticalSpeedAnalysis._Cast_CouplingHalfCompoundCriticalSpeedAnalysis":
        return self._Cast_CouplingHalfCompoundCriticalSpeedAnalysis(self)

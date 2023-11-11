"""CouplingHalfCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5320,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5151,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingHalfCompoundModalAnalysisAtASpeed")


class CouplingHalfCompoundModalAnalysisAtASpeed(
    _5320.MountableComponentCompoundModalAnalysisAtASpeed
):
    """CouplingHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CouplingHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
            parent: "CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5320.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(_5266.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(_5335.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5151.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5151.CouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingHalfModalAnalysisAtASpeed]

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
    ) -> "CouplingHalfCompoundModalAnalysisAtASpeed._Cast_CouplingHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_CouplingHalfCompoundModalAnalysisAtASpeed(self)

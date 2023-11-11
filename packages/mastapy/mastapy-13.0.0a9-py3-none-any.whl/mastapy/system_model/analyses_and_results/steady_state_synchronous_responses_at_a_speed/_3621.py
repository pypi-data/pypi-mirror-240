"""TorqueConverterSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3540,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6970


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterSteadyStateSynchronousResponseAtASpeed")


class TorqueConverterSteadyStateSynchronousResponseAtASpeed(
    _3540.CouplingSteadyStateSynchronousResponseAtASpeed
):
    """TorqueConverterSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting TorqueConverterSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
            parent: "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3540.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3501,
            )

            return self._parent._cast(
                _3501.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
        ) -> "TorqueConverterSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "TorqueConverterSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6970.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterSteadyStateSynchronousResponseAtASpeed._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_TorqueConverterSteadyStateSynchronousResponseAtASpeed(self)

"""RollingRingAssemblySteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3340,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="RollingRingAssemblySteadyStateSynchronousResponseOnAShaft"
)


class RollingRingAssemblySteadyStateSynchronousResponseOnAShaft(
    _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
):
    """RollingRingAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RollingRingAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6942.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "RollingRingAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RollingRingAssemblySteadyStateSynchronousResponseOnAShaft(
            self
        )

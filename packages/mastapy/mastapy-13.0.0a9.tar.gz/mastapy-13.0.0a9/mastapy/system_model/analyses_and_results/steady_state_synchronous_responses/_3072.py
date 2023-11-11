"""RollingRingAssemblySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3079,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "RollingRingAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6942


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="RollingRingAssemblySteadyStateSynchronousResponse")


class RollingRingAssemblySteadyStateSynchronousResponse(
    _3079.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """RollingRingAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_RollingRingAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting RollingRingAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
            parent: "RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
        ) -> "RollingRingAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "RollingRingAssemblySteadyStateSynchronousResponse.TYPE",
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
    ) -> "RollingRingAssemblySteadyStateSynchronousResponse._Cast_RollingRingAssemblySteadyStateSynchronousResponse":
        return self._Cast_RollingRingAssemblySteadyStateSynchronousResponse(self)

"""ClutchSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3019,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ClutchSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.static_loads import _6831


__docformat__ = "restructuredtext en"
__all__ = ("ClutchSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ClutchSteadyStateSynchronousResponse")


class ClutchSteadyStateSynchronousResponse(
    _3019.CouplingSteadyStateSynchronousResponse
):
    """ClutchSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CLUTCH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchSteadyStateSynchronousResponse")

    class _Cast_ClutchSteadyStateSynchronousResponse:
        """Special nested class for casting ClutchSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
            parent: "ClutchSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3019.CouplingSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
        ) -> "ClutchSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ClutchSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6831.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

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
    ) -> "ClutchSteadyStateSynchronousResponse._Cast_ClutchSteadyStateSynchronousResponse":
        return self._Cast_ClutchSteadyStateSynchronousResponse(self)

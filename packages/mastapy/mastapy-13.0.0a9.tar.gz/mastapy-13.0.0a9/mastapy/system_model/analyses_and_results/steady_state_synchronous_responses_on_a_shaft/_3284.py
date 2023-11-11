"""CVTSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3252,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CVTSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583


__docformat__ = "restructuredtext en"
__all__ = ("CVTSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CVTSteadyStateSynchronousResponseOnAShaft")


class CVTSteadyStateSynchronousResponseOnAShaft(
    _3252.BeltDriveSteadyStateSynchronousResponseOnAShaft
):
    """CVTSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CVTSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CVTSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
            parent: "CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3252.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
        ) -> "CVTSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "CVTSteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTSteadyStateSynchronousResponseOnAShaft._Cast_CVTSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CVTSteadyStateSynchronousResponseOnAShaft(self)

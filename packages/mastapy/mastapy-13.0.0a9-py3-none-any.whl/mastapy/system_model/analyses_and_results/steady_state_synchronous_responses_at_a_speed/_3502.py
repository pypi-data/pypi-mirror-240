"""AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3526,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"
)


class AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed(
    _3526.ComponentSteadyStateSynchronousResponseAtASpeed
):
    """AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3503,
            )

            return self._parent._cast(
                _3503.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(_3597.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed(
            self
        )

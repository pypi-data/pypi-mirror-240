"""CouplingConnectionCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3178,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CouplingConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3017,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundSteadyStateSynchronousResponse")


class CouplingConnectionCompoundSteadyStateSynchronousResponse(
    _3178.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
):
    """CouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
            parent: "CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3178.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3135,
            )

            return self._parent._cast(
                _3135.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "CouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3017.CouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3017.CouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CouplingConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_CouplingConnectionCompoundSteadyStateSynchronousResponse(self)

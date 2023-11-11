"""PlanetaryGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3162,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3065,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundSteadyStateSynchronousResponse")


class PlanetaryGearSetCompoundSteadyStateSynchronousResponse(
    _3162.CylindricalGearSetCompoundSteadyStateSynchronousResponse
):
    """PlanetaryGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PlanetaryGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
            parent: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3162.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3113,
            )

            return self._parent._cast(
                _3113.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PlanetaryGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3065.PlanetaryGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3065.PlanetaryGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PlanetaryGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundSteadyStateSynchronousResponse._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_PlanetaryGearSetCompoundSteadyStateSynchronousResponse(self)

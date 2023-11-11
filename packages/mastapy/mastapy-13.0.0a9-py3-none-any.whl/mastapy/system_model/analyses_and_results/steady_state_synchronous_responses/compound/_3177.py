"""HypoidGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3119,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "HypoidGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3044,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3175,
        _3176,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundSteadyStateSynchronousResponse")


class HypoidGearSetCompoundSteadyStateSynchronousResponse(
    _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
):
    """HypoidGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
            parent: "HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3113,
            )

            return self._parent._cast(
                _3113.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "HypoidGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "HypoidGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2532.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3044.HypoidGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearSetSteadyStateSynchronousResponse]

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
    def hypoid_gears_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3175.HypoidGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.HypoidGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3176.HypoidGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.HypoidGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3044.HypoidGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearSetSteadyStateSynchronousResponse]

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
    ) -> "HypoidGearSetCompoundSteadyStateSynchronousResponse._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponse(self)

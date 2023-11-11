"""HypoidGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2985,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "HypoidGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6904
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3045,
        _3043,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="HypoidGearSetSteadyStateSynchronousResponse")


class HypoidGearSetSteadyStateSynchronousResponse(
    _2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
):
    """HypoidGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_HypoidGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
            parent: "HypoidGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
        ) -> "HypoidGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "HypoidGearSetSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self: Self) -> "_6904.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3045.HypoidGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3043.HypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.HypoidGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse":
        return self._Cast_HypoidGearSetSteadyStateSynchronousResponse(self)

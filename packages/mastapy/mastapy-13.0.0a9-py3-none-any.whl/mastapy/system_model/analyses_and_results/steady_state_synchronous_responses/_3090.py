"""StraightBevelDiffGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2997,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelDiffGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3091,
        _3089,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetSteadyStateSynchronousResponse")


class StraightBevelDiffGearSetSteadyStateSynchronousResponse(
    _2997.BevelGearSetSteadyStateSynchronousResponse
):
    """StraightBevelDiffGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelDiffGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
            parent: "StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_2997.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
        ) -> "StraightBevelDiffGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelDiffGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3091.StraightBevelDiffGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3089.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponse(self)

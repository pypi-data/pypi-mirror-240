"""ConicalGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3040,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConicalGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearSetSteadyStateSynchronousResponse")


class ConicalGearSetSteadyStateSynchronousResponse(
    _3040.GearSetSteadyStateSynchronousResponse
):
    """ConicalGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
            parent: "ConicalGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3040.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2980,
            )

            return self._parent._cast(
                _2980.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(_2997.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
        ) -> "ConicalGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConicalGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2521.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

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
    ) -> "ConicalGearSetSteadyStateSynchronousResponse._Cast_ConicalGearSetSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearSetSteadyStateSynchronousResponse(self)

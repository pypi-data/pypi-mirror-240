"""StraightBevelDiffGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2998,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelDiffGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6956


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSteadyStateSynchronousResponse")


class StraightBevelDiffGearSteadyStateSynchronousResponse(
    _2998.BevelGearSteadyStateSynchronousResponse
):
    """StraightBevelDiffGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelDiffGearSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelDiffGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
            parent: "StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_2998.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
        ) -> "StraightBevelDiffGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelDiffGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6956.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelDiffGearSteadyStateSynchronousResponse(self)

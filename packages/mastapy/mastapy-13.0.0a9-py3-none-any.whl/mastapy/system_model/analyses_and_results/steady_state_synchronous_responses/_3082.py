"""SpiralBevelGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2998,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpiralBevelGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import _6950


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpiralBevelGearSteadyStateSynchronousResponse")


class SpiralBevelGearSteadyStateSynchronousResponse(
    _2998.BevelGearSteadyStateSynchronousResponse
):
    """SpiralBevelGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSteadyStateSynchronousResponse"
    )

    class _Cast_SpiralBevelGearSteadyStateSynchronousResponse:
        """Special nested class for casting SpiralBevelGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
            parent: "SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_2998.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "SpiralBevelGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpiralBevelGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6950.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearSteadyStateSynchronousResponse._Cast_SpiralBevelGearSteadyStateSynchronousResponse":
        return self._Cast_SpiralBevelGearSteadyStateSynchronousResponse(self)

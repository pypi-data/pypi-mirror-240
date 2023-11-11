"""AGMAGleasonConicalGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3014,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSteadyStateSynchronousResponse")


class AGMAGleasonConicalGearSteadyStateSynchronousResponse(
    _3014.ConicalGearSteadyStateSynchronousResponse
):
    """AGMAGleasonConicalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse"
    )

    class _Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse:
        """Special nested class for casting AGMAGleasonConicalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
            parent: "AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(
                _2993.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2994,
            )

            return self._parent._cast(
                _2994.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.BevelGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.HypoidGearSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3091,
            )

            return self._parent._cast(
                _3091.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3095,
            )

            return self._parent._cast(
                _3095.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(
                _3112.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
        ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AGMAGleasonConicalGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2510.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearSteadyStateSynchronousResponse._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse":
        return self._Cast_AGMAGleasonConicalGearSteadyStateSynchronousResponse(self)

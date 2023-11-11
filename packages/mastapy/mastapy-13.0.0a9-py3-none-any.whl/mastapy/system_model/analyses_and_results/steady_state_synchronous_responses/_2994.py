"""BevelDifferentialPlanetGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2993,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearSteadyStateSynchronousResponse"
)


class BevelDifferentialPlanetGearSteadyStateSynchronousResponse(
    _2993.BevelDifferentialGearSteadyStateSynchronousResponse
):
    """BevelDifferentialPlanetGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialPlanetGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
            parent: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2993.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(_2998.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialPlanetGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2514.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse(
            self
        )

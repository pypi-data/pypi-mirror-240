"""KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3014,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse"
)


class KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse(
    _3014.ConicalGearSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3014.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse(
            self
        )

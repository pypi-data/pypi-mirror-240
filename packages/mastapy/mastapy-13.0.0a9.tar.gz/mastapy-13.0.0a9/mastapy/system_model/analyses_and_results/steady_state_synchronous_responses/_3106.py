"""VirtualComponentSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3058,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "VirtualComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="VirtualComponentSteadyStateSynchronousResponse")


class VirtualComponentSteadyStateSynchronousResponse(
    _3058.MountableComponentSteadyStateSynchronousResponse
):
    """VirtualComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentSteadyStateSynchronousResponse"
    )

    class _Cast_VirtualComponentSteadyStateSynchronousResponse:
        """Special nested class for casting VirtualComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
            parent: "VirtualComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3058.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(_3060.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3056,
            )

            return self._parent._cast(_3056.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def point_load_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(_3068.PowerLoadSteadyStateSynchronousResponse)

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
        ) -> "VirtualComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse",
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
        instance_to_wrap: "VirtualComponentSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2476.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentSteadyStateSynchronousResponse._Cast_VirtualComponentSteadyStateSynchronousResponse":
        return self._Cast_VirtualComponentSteadyStateSynchronousResponse(self)

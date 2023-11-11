"""ConicalGearMeshCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3172,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3012,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundSteadyStateSynchronousResponse")


class ConicalGearMeshCompoundSteadyStateSynchronousResponse(
    _3172.GearMeshCompoundSteadyStateSynchronousResponse
):
    """ConicalGearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConicalGearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
            parent: "ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3172.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3125,
            )

            return self._parent._cast(
                _3125.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
        ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConicalGearMeshCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.ConicalGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3012.ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3012.ConicalGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConicalGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCompoundSteadyStateSynchronousResponse._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse":
        return self._Cast_ConicalGearMeshCompoundSteadyStateSynchronousResponse(self)

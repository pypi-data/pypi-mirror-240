"""CylindricalGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3561,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.static_loads import _6858


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearSteadyStateSynchronousResponseAtASpeed")


class CylindricalGearSteadyStateSynchronousResponseAtASpeed(
    _3561.GearSteadyStateSynchronousResponseAtASpeed
):
    """CylindricalGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
            parent: "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(_3561.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(_3580.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CylindricalGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2522.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6858.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CylindricalGearSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CylindricalGearSteadyStateSynchronousResponseAtASpeed(self)

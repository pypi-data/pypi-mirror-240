"""CylindricalGearSetSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3301,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3291,
        _3289,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CylindricalGearSetSteadyStateSynchronousResponseOnAShaft")


class CylindricalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3301.GearSetSteadyStateSynchronousResponseOnAShaft
):
    """CylindricalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CylindricalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3301.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2523.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6862.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3291.CylindricalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3289.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CylindricalGearSetSteadyStateSynchronousResponseOnAShaft(self)

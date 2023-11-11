"""CouplingSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3340,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingSteadyStateSynchronousResponseOnAShaft")


class CouplingSteadyStateSynchronousResponseOnAShaft(
    _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
):
    """CouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CouplingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3340.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3242,
            )

            return self._parent._cast(
                _3242.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(_3321.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(
                _3265.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingSteadyStateSynchronousResponseOnAShaft(self)

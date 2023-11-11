"""AbstractAssemblyCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3192,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2980,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundSteadyStateSynchronousResponse")


class AbstractAssemblyCompoundSteadyStateSynchronousResponse(
    _3192.PartCompoundSteadyStateSynchronousResponse
):
    """AbstractAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3192.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3119,
            )

            return self._parent._cast(
                _3119.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3123,
            )

            return self._parent._cast(
                _3123.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3133,
            )

            return self._parent._cast(
                _3133.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(_3154.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2980.AbstractAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2980.AbstractAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractAssemblySteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse(self)

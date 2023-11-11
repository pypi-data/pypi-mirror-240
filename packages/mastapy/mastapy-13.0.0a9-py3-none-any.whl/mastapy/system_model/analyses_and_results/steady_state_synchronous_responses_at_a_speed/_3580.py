"""PartSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3606,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PartSteadyStateSynchronousResponseAtASpeed")


class PartSteadyStateSynchronousResponseAtASpeed(_7544.PartStaticLoadAnalysisCase):
    """PartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_PartSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
            parent: "PartSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3501,
            )

            return self._parent._cast(
                _3501.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3503,
            )

            return self._parent._cast(
                _3503.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3509,
            )

            return self._parent._cast(
                _3509.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3515,
            )

            return self._parent._cast(
                _3515.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3520,
            )

            return self._parent._cast(
                _3520.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(_3521.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(
                _3524.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(_3543.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3544,
            )

            return self._parent._cast(
                _3544.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3551,
            )

            return self._parent._cast(
                _3551.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(_3552.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3557,
            )

            return self._parent._cast(
                _3557.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(_3561.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(
                _3587.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3596,
            )

            return self._parent._cast(
                _3596.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(_3597.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
        ) -> "PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "PartSteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "_3606.SteadyStateSynchronousResponseAtASpeed":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SteadyStateSynchronousResponseAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartSteadyStateSynchronousResponseAtASpeed(self)

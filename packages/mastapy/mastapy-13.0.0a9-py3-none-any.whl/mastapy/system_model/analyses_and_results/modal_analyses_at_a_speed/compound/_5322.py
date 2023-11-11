"""PartCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "PartCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5193,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PartCompoundModalAnalysisAtASpeed")


class PartCompoundModalAnalysisAtASpeed(_7542.PartCompoundAnalysis):
    """PartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundModalAnalysisAtASpeed")

    class _Cast_PartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
            parent: "PartCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5243,
            )

            return self._parent._cast(
                _5243.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5244,
            )

            return self._parent._cast(_5244.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5245,
            )

            return self._parent._cast(
                _5245.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(_5250.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(_5251.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(_5253.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5254,
            )

            return self._parent._cast(
                _5254.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(
                _5256.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(
                _5257.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(_5259.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(_5261.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(_5262.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(_5266.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(_5274.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(_5275.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(_5285.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(
                _5286.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(
                _5292.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(
                _5293.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(_5294.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(_5296.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(_5299.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(
                _5300.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(
                _5309.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(
                _5311.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(_5318.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(_5321.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(
                _5325.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(_5328.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(_5329.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(_5331.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(
                _5334.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(_5335.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(_5337.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(_5338.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(
                _5339.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(_5345.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(_5356.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(
                _5360.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(_5364.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(_5366.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(_5369.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
        ) -> "PartCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PartCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5193.PartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5193.PartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundModalAnalysisAtASpeed._Cast_PartCompoundModalAnalysisAtASpeed":
        return self._Cast_PartCompoundModalAnalysisAtASpeed(self)

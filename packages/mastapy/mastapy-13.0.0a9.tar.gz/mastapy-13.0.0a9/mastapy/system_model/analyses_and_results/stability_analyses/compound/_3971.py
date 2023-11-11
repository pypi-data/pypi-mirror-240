"""MountableComponentCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3919
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "MountableComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3839


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundStabilityAnalysis")


class MountableComponentCompoundStabilityAnalysis(
    _3919.ComponentCompoundStabilityAnalysis
):
    """MountableComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundStabilityAnalysis"
    )

    class _Cast_MountableComponentCompoundStabilityAnalysis:
        """Special nested class for casting MountableComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
            parent: "MountableComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3919.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(
                _3898.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bearing_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(_3902.BearingCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(
                _3905.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(_3910.BevelGearCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConicalGearCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(
                _3944.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def face_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(_3947.FaceGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.GearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def oil_seal_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(
                _3976.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planet_carrier_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.RollingRingCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(_3990.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(
                _3999.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(_4002.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(
                _4005.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(
                _4014.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(_4017.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "MountableComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3839.MountableComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MountableComponentStabilityAnalysis]

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
    ) -> "List[_3839.MountableComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MountableComponentStabilityAnalysis]

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
    ) -> "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis":
        return self._Cast_MountableComponentCompoundStabilityAnalysis(self)

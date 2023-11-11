"""MountableComponentStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "MountableComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="MountableComponentStabilityAnalysis")


class MountableComponentStabilityAnalysis(_3785.ComponentStabilityAnalysis):
    """MountableComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentStabilityAnalysis")

    class _Cast_MountableComponentStabilityAnalysis:
        """Special nested class for casting MountableComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
            parent: "MountableComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(_3768.BearingStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(
                _3774.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTPulleyStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.FaceGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3830,
            )

            return self._parent._cast(
                _3830.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(_3838.MeasurementComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def planet_carrier_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(_3857.ShaftHubConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "MountableComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

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
    ) -> (
        "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis"
    ):
        return self._Cast_MountableComponentStabilityAnalysis(self)

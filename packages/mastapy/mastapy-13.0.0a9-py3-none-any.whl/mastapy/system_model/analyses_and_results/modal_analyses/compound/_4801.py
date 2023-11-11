"""MountableComponentCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "MountableComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4654


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysis")


class MountableComponentCompoundModalAnalysis(_4749.ComponentCompoundModalAnalysis):
    """MountableComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundModalAnalysis"
    )

    class _Cast_MountableComponentCompoundModalAnalysis:
        """Special nested class for casting MountableComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
            parent: "MountableComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            return self._parent._cast(_4749.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.BearingCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(
                _4738.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(
                _4739.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.BevelGearCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConicalGearCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConnectorCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CVTPulleyCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(_4774.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.FaceGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.GearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(
                _4790.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(_4799.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(_4800.MeasurementComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(
                _4806.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planet_carrier_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(_4810.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.RollingRingCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(_4839.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.ZerolBevelGearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "MountableComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4654.MountableComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    ) -> "List[_4654.MountableComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    ) -> "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis":
        return self._Cast_MountableComponentCompoundModalAnalysis(self)

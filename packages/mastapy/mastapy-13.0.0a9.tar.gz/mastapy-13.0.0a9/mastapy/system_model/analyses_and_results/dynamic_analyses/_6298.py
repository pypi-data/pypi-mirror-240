"""ComponentDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441


__docformat__ = "restructuredtext en"
__all__ = ("ComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="ComponentDynamicAnalysis")


class ComponentDynamicAnalysis(_6354.PartDynamicAnalysis):
    """ComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentDynamicAnalysis")

    class _Cast_ComponentDynamicAnalysis:
        """Special nested class for casting ComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
            parent: "ComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6274

            return self._parent._cast(_6274.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275

            return self._parent._cast(_6275.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.BearingDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelGearDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BoltDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ConceptGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConicalGearDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectorDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.CouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6323

            return self._parent._cast(_6323.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.FaceGearDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.FEPartDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.GearDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(_6350.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(_6351.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RollingRingDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6371

            return self._parent._cast(_6371.ShaftHubConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.SpiralBevelGearDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.WormGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.ZerolBevelGearDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis",
        ) -> "ComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentDynamicAnalysis._Cast_ComponentDynamicAnalysis":
        return self._Cast_ComponentDynamicAnalysis(self)

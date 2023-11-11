"""SQLDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQL_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "SQLDatabase")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1823
    from mastapy import _0


__docformat__ = "restructuredtext en"
__all__ = ("SQLDatabase",)


Self = TypeVar("Self", bound="SQLDatabase")
TKey = TypeVar("TKey", bound="_1823.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")


class SQLDatabase(_1821.Database[TKey, TValue]):
    """SQLDatabase

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _SQL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SQLDatabase")

    class _Cast_SQLDatabase:
        """Special nested class for casting SQLDatabase to subclasses."""

        def __init__(self: "SQLDatabase._Cast_SQLDatabase", parent: "SQLDatabase"):
            self._parent = parent

        @property
        def database(self: "SQLDatabase._Cast_SQLDatabase"):
            return self._parent._cast(_1821.Database)

        @property
        def shaft_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.materials import _244

            return self._parent._cast(_244.BearingMaterialDatabase)

        @property
        def component_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.materials import _247

            return self._parent._cast(_247.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.materials import _266

            return self._parent._cast(_266.LubricationDetailDatabase)

        @property
        def material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.materials import _268

            return self._parent._cast(_268.MaterialDatabase)

        @property
        def materials_settings_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears import _341

            return self._parent._cast(_341.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.rating.cylindrical import _451

            return self._parent._cast(
                _451.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _582

            return self._parent._cast(_582.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.materials import _584

            return self._parent._cast(_584.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _587

            return self._parent._cast(_587.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _597

            return self._parent._cast(
                _597.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.materials import _605

            return self._parent._cast(_605.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.cylindrical import _608

            return self._parent._cast(_608.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.cylindrical import _613

            return self._parent._cast(_613.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703

            return self._parent._cast(_703.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.gears.manufacturing.bevel import _798

            return self._parent._cast(_798.ManufacturingMachineDatabase)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _918

            return self._parent._cast(
                _918.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _919

            return self._parent._cast(
                _919.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _923

            return self._parent._cast(
                _923.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(_927.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(
                _933.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_designs import _938

            return self._parent._cast(_938.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_designs import _940

            return self._parent._cast(_940.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_designs import _943

            return self._parent._cast(_943.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1013

            return self._parent._cast(_1013.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1019

            return self._parent._cast(
                _1019.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.electric_machines import _1280

            return self._parent._cast(_1280.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.electric_machines import _1298

            return self._parent._cast(_1298.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.electric_machines import _1311

            return self._parent._cast(_1311.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.cycloidal import _1453

            return self._parent._cast(_1453.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.cycloidal import _1460

            return self._parent._cast(_1460.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bolts import _1463

            return self._parent._cast(_1463.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bolts import _1465

            return self._parent._cast(_1465.BoltGeometryDatabase)

        @property
        def bolt_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bolts import _1467

            return self._parent._cast(_1467.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bolts import _1472

            return self._parent._cast(_1472.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.math_utility.optimisation import _1536

            return self._parent._cast(_1536.DesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.math_utility.optimisation import _1538

            return self._parent._cast(
                _1538.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.math_utility.optimisation import _1549

            return self._parent._cast(_1549.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.utility.databases import _1825

            return self._parent._cast(_1825.NamedDatabase)

        @property
        def bearing_settings_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bearings import _1877

            return self._parent._cast(_1877.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bearings import _1890

            return self._parent._cast(_1890.RollingBearingDatabase)

        @property
        def iso14179_settings_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.bearings.bearing_results.rolling import _1972

            return self._parent._cast(_1972.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ):
            from mastapy.system_model.optimization import _2225

            return self._parent._cast(_2225.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.system_model.optimization import _2233

            return self._parent._cast(_2233.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(self: "SQLDatabase._Cast_SQLDatabase"):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2561,
            )

            return self._parent._cast(_2561.SuperchargerRotorSetDatabase)

        @property
        def sql_database(self: "SQLDatabase._Cast_SQLDatabase") -> "SQLDatabase":
            return self._parent

        def __getattr__(self: "SQLDatabase._Cast_SQLDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SQLDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_network_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def uses_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UsesDatabase

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def delete(self: Self, key: "TKey"):
        """Method does not return.

        Args:
            key (TKey)
        """
        self.wrapped.Delete(key)

    def reload(self: Self):
        """Method does not return."""
        self.wrapped.Reload()

    @enforce_parameter_types
    def save(self: Self, item: "TValue"):
        """Method does not return.

        Args:
            item (TValue)
        """
        self.wrapped.Save(item)

    @property
    def cast_to(self: Self) -> "SQLDatabase._Cast_SQLDatabase":
        return self._Cast_SQLDatabase(self)

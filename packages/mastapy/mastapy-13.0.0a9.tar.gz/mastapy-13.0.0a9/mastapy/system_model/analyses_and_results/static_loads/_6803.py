"""AbstractAssemblyLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6925
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyLoadCase",)


Self = TypeVar("Self", bound="AbstractAssemblyLoadCase")


class AbstractAssemblyLoadCase(_6925.PartLoadCase):
    """AbstractAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyLoadCase")

    class _Cast_AbstractAssemblyLoadCase:
        """Special nested class for casting AbstractAssemblyLoadCase to subclasses."""

        def __init__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
            parent: "AbstractAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AssemblyLoadCase)

        @property
        def belt_drive_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(
                _6911.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.RollingRingAssemblyLoadCase)

        @property
        def root_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(_6945.RootAssemblyLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "AbstractAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2431.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2431.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

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
    ) -> "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase":
        return self._Cast_AbstractAssemblyLoadCase(self)

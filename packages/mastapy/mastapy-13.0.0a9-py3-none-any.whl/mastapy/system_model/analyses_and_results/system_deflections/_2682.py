"""AbstractAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431
    from mastapy.system_model.analyses_and_results.system_deflections import _2712
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2845,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4029


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySystemDeflection",)


Self = TypeVar("Self", bound="AbstractAssemblySystemDeflection")


class AbstractAssemblySystemDeflection(_2782.PartSystemDeflection):
    """AbstractAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblySystemDeflection")

    class _Cast_AbstractAssemblySystemDeflection:
        """Special nested class for casting AbstractAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            parent: "AbstractAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def part_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AssemblySystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearSetSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BoltedJointSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearSetSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingSystemDeflection)

        @property
        def cvt_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CycloidalAssemblySystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearSetSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.RollingRingAssemblySystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RootAssemblySystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearSetSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearSetSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearSetSystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
        ) -> "AbstractAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblySystemDeflection.TYPE"):
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
    def components_with_unknown_mass_properties(
        self: Self,
    ) -> "List[_2712.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithUnknownMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def components_with_zero_mass_properties(
        self: Self,
    ) -> "List[_2712.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentsWithZeroMassProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigidly_connected_groups(
        self: Self,
    ) -> "List[_2845.RigidlyConnectedComponentGroupSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.RigidlyConnectedComponentGroupSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4029.AbstractAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblySystemDeflection._Cast_AbstractAssemblySystemDeflection":
        return self._Cast_AbstractAssemblySystemDeflection(self)

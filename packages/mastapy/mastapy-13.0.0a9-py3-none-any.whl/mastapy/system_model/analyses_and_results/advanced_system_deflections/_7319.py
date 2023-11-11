"""CylindricalGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7331
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.gears.rating.cylindrical import _462
    from mastapy.gears.gear_designs.cylindrical import _1026
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1105
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7317,
        _7318,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearSetAdvancedSystemDeflection")


class CylindricalGearSetAdvancedSystemDeflection(_7331.GearSetAdvancedSystemDeflection):
    """CylindricalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearSetAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
            parent: "CylindricalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7331.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7266,
            )

            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "CylindricalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2523.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6862.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_462.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_462.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_design(self: Self) -> "_1026.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry(self: Self) -> "_1105.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7317.CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7318.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection":
        return self._Cast_CylindricalGearSetAdvancedSystemDeflection(self)

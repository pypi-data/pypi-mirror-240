"""HypoidGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "HypoidGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6904
    from mastapy.gears.rating.hypoid import _438
    from mastapy.system_model.analyses_and_results.system_deflections import _2761
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7333,
        _7334,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearSetAdvancedSystemDeflection")


class HypoidGearSetAdvancedSystemDeflection(
    _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
):
    """HypoidGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetAdvancedSystemDeflection"
    )

    class _Cast_HypoidGearSetAdvancedSystemDeflection:
        """Special nested class for casting HypoidGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
            parent: "HypoidGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7266,
            )

            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "HypoidGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "HypoidGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2532.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6904.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2761.HypoidGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7333.HypoidGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7334.HypoidGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection":
        return self._Cast_HypoidGearSetAdvancedSystemDeflection(self)

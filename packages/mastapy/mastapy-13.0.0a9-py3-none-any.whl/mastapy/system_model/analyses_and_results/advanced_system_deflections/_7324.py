"""FaceGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "FaceGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.gears.rating.face import _446
    from mastapy.system_model.analyses_and_results.static_loads import _6881
    from mastapy.system_model.analyses_and_results.system_deflections import _2753


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearAdvancedSystemDeflection")


class FaceGearAdvancedSystemDeflection(_7329.GearAdvancedSystemDeflection):
    """FaceGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearAdvancedSystemDeflection")

    class _Cast_FaceGearAdvancedSystemDeflection:
        """Special nested class for casting FaceGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
            parent: "FaceGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7329.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def face_gear_advanced_system_deflection(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
        ) -> "FaceGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_446.FaceGearRating":
        """mastapy.gears.rating.face.FaceGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2753.FaceGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearAdvancedSystemDeflection._Cast_FaceGearAdvancedSystemDeflection":
        return self._Cast_FaceGearAdvancedSystemDeflection(self)

"""StraightBevelSunGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelSunGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelSunGearAdvancedSystemDeflection")


class StraightBevelSunGearAdvancedSystemDeflection(
    _7377.StraightBevelDiffGearAdvancedSystemDeflection
):
    """StraightBevelSunGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelSunGearAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelSunGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
            parent: "StraightBevelSunGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7377.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(_7285.BevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(
                _7273.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
        ) -> "StraightBevelSunGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "StraightBevelSunGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "StraightBevelSunGearAdvancedSystemDeflection._Cast_StraightBevelSunGearAdvancedSystemDeflection":
        return self._Cast_StraightBevelSunGearAdvancedSystemDeflection(self)

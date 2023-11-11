"""ConicalGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearAdvancedSystemDeflection")


class ConicalGearAdvancedSystemDeflection(_7329.GearAdvancedSystemDeflection):
    """ConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearAdvancedSystemDeflection")

    class _Cast_ConicalGearAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
            parent: "ConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7329.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(
                _7273.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(
                _7280.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(
                _7283.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(_7285.BevelGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(
                _7340.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(
                _7377.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "ConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection"
    ):
        return self._Cast_ConicalGearAdvancedSystemDeflection(self)
